import streamlit as st
import pandas as pd
import os
import plotly.express as px
import numpy as np

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Elite Intern Dashboard", layout="wide")

# -------------------------------
# LOAD DATA
# -------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "data", "cleaned_intern_data_final.csv")
df = pd.read_csv(file_path)

# -------------------------------
# ADD FIELDS
# -------------------------------
if "Gender" not in df.columns:
    df["Gender"] = np.random.choice(["Male", "Female"], len(df))

df["Communication_Score"] = df["Feedback_Score"] * 2
df["Obedience_Score"] = df["Feedback_Score"] * 2

df["Before_Deadline_Completion (%)"] = (
    df["Deadline_Adherence (%)"] * 0.8 +
    df["Completion_Rate"] * 0.2
)

max_duration = df["Duration_Days"].max()
df["Duration_Efficiency"] = (max_duration - df["Duration_Days"]) / max_duration * 100

# -------------------------------
# 🎯 PRIORITY SCORE (FINAL BALANCED MODEL)
# -------------------------------
df["Priority_Score"] = (
    df["Completion_Rate"] * 0.20 +
    df["Attendance (%)"] * 0.20 +
    df["Quality_Score"] * 0.20 +
    df["Before_Deadline_Completion (%)"] * 0.20 +
    df["Projects_Completed"] * 2 +
    df["Duration_Efficiency"] * 0.10 +
    df["Obedience_Score"] * 0.10
)

# -------------------------------
# 🧠 HIRING RECOMMENDATION SYSTEM
# -------------------------------
def hiring_decision(row):
    if (
        row["Priority_Score"] > 85 and
        row["Attendance (%)"] > 90 and
        row["Quality_Score"] > 8
    ):
        return "🟢 Hire Immediately"
    elif row["Priority_Score"] > 70:
        return "🟡 Consider for Hiring"
    else:
        return "🔴 Needs Improvement"

df["Hiring_Status"] = df.apply(hiring_decision, axis=1)

# -------------------------------
# IMAGE FUNCTION
# -------------------------------
def get_image(gender):
    return (
        "https://cdn-icons-png.flaticon.com/512/4140/4140048.png"
        if gender == "Female"
        else "https://cdn-icons-png.flaticon.com/512/4140/4140051.png"
    )

dept_logo = {
    "Data Science": "📊",
    "Marketing": "📢",
    "HR": "👥",
    "Finance": "💰",
    "Operations": "⚙️"
}

rank_colors = {1: "#FFD700", 2: "#C0C0C0", 3: "#CD7F32"}
rank_icons = {1: "🥇", 2: "🥈", 3: "🥉"}

# -------------------------------
# 💎 PREMIUM UI CSS (SaaS LEVEL)
# -------------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #020617, #0f172a);
    color: white;
}

/* KPI Cards */
.card {
    background: linear-gradient(145deg, #111827, #1f2937);
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 0 20px rgba(0,255,200,0.2);
}

/* Profile Cards */
.profile {
    background: linear-gradient(135deg, #020617, #111827);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 0 25px rgba(0,200,255,0.3);
    transition: 0.3s;
}
.profile:hover {
    transform: scale(1.05);
    box-shadow: 0 0 35px rgba(0,200,255,0.8);
}

.rank {
    font-size: 22px;
    font-weight: bold;
}

.section {
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# TITLE
# -------------------------------
st.title("🚀 Intern Performance Intelligence System")

# -------------------------------
# FILTERS
# -------------------------------
st.sidebar.header("🔍 Filters")

dept = st.sidebar.selectbox("Department", ["All"] + list(df['Department'].unique()))
mentor = st.sidebar.selectbox("Mentor", ["All"] + list(df['Mentor'].unique()))

filtered_df = df.copy()

if dept != "All":
    filtered_df = filtered_df[filtered_df['Department'] == dept]

if mentor != "All":
    filtered_df = filtered_df[filtered_df['Mentor'] == mentor]

# -------------------------------
# KPI SECTION
# -------------------------------
st.subheader("📊 Core KPIs")

col1, col2, col3 = st.columns(3)

def kpi(col, title, value):
    col.markdown(f"""
    <div class="card">
        <h4>{title}</h4>
        <h2 style="color:#00FFC6;">{value}</h2>
    </div>
    """, unsafe_allow_html=True)

kpi(col1, "Completion Rate", f"{round(filtered_df['Completion_Rate'].mean(),2)}%")
kpi(col2, "Attendance", f"{round(filtered_df['Attendance (%)'].mean(),2)}%")
kpi(col3, "Quality Score", round(filtered_df['Quality_Score'].mean(),2))

# -------------------------------
# TOP 3 GLOBAL
# -------------------------------
top3_global = filtered_df.sort_values(by="Priority_Score", ascending=False).head(3)
top3_global["Rank"] = [1, 2, 3]

# -------------------------------
# 📈 SCATTER (TOP 3 HIGHLIGHT)
# -------------------------------
st.subheader("📈 Performance Insights")

fig = px.scatter(
    filtered_df,
    x="Completion_Rate",
    y="Quality_Score",
    size="Projects_Completed",
    color="Department",
    hover_data=["Name", "Attendance (%)", "Priority_Score"]
)

for _, row in top3_global.iterrows():
    fig.add_scatter(
        x=[row["Completion_Rate"]],
        y=[row["Quality_Score"]],
        mode="markers+text",
        marker=dict(
            size=30,
            color=rank_colors[row["Rank"]],
            line=dict(width=3, color="white")
        ),
        text=[f"{rank_icons[row['Rank']]} {row['Name']}"],
        textposition="top center"
    )

fig.update_layout(template="plotly_dark",
                  xaxis_title="Completion Rate (%)",
                  yaxis_title="Quality Score")

st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# 💼 HIRING OVERVIEW
# -------------------------------
st.subheader("💼 Hiring Recommendation")

fig_hiring = px.pie(
    filtered_df,
    names="Hiring_Status",
    color="Hiring_Status",
    color_discrete_map={
        "🟢 Hire Immediately": "green",
        "🟡 Consider for Hiring": "orange",
        "🔴 Needs Improvement": "red"
    }
)

fig_hiring.update_layout(template="plotly_dark")
st.plotly_chart(fig_hiring, use_container_width=True)
# -------------------------------
# 🎯 TOP HIRING RECOMMENDATIONS (WHAT + WHY)
# -------------------------------
st.subheader("🎯 Top Hiring Recommendations (AI-Driven)")

# Get TOP 3 based on FILTERED DATA
top_hires = filtered_df.sort_values(by="Priority_Score", ascending=False).head(3)

def suggest_role(row):
    if row["Department"] == "Data Science":
        return "Data Analyst / ML Engineer"
    elif row["Department"] == "Marketing":
        return "Digital Marketing Specialist"
    elif row["Department"] == "HR":
        return "HR Executive"
    elif row["Department"] == "Finance":
        return "Financial Analyst"
    elif row["Department"] == "Operations":
        return "Operations Manager"
    return "General Role"

def hire_reason(row):
    reasons = []

    if row["Completion_Rate"] > 85:
        reasons.append("High Productivity")

    if row["Attendance (%)"] > 90:
        reasons.append("Excellent Consistency")

    if row["Quality_Score"] > 8:
        reasons.append("High Quality Output")

    if row["Before_Deadline_Completion (%)"] > 85:
        reasons.append("Proactive Delivery")

    if row["Duration_Efficiency"] > 70:
        reasons.append("Fast Execution")

    return ", ".join(reasons)

# Display cards
cols = st.columns(3)

for i, (_, row) in enumerate(top_hires.iterrows()):
    with cols[i]:

        st.markdown(f"""
        <div class="profile">
        <div class="rank" style="color:{rank_colors[i+1]}">
            {rank_icons[i+1]} Recommended Hire #{i+1}
        </div>

        <h3>{row['Name']}</h3>

        💼 Role Fit: <b>{suggest_role(row)}</b> <br><br>

        📊 WHY HIRE?<br>
        {hire_reason(row)}

        <hr>

        🏆 Priority Score: {round(row['Priority_Score'],2)} <br>
        📈 Completion: {round(row['Completion_Rate'],2)}% <br>
        🟢 Attendance: {row['Attendance (%)']}% <br>
        ⭐ Quality: {row['Quality_Score']}
        </div>
        """, unsafe_allow_html=True)

# -------------------------------
# 🤖 AI INSIGHTS PANEL
# -------------------------------
st.subheader("🤖 AI Insights")

st.markdown(f"""
✔ Avg Completion: **{round(filtered_df['Completion_Rate'].mean(),2)}%**  
✔ Avg Attendance: **{round(filtered_df['Attendance (%)'].mean(),2)}%**  
✔ Avg Quality: **{round(filtered_df['Quality_Score'].mean(),2)}**

🏆 Best Dept: **{filtered_df.groupby('Department')['Priority_Score'].mean().idxmax()}**  
⚠️ Weak Dept: **{filtered_df.groupby('Department')['Priority_Score'].mean().idxmin()}**

💡 Recommendation:
- Improve attendance consistency  
- Improve quality  
- Focus on deadline adherence  
""")

# -------------------------------
# 🏆 DEPARTMENT CHAMPIONS
# -------------------------------
st.subheader("🏆 Department Champions")

for dept_name in filtered_df['Department'].unique():

    st.markdown(f"### {dept_logo.get(dept_name)} {dept_name}")

    dept_df = filtered_df[filtered_df['Department'] == dept_name]
    top3 = dept_df.sort_values(by='Priority_Score', ascending=False).head(3)

    cols = st.columns(3)

    for i, (_, row) in enumerate(top3.iterrows()):
        with cols[i]:

            st.image(get_image(row["Gender"]), width=100)

            st.markdown(f"""
            <div class="profile">
            <div class="rank" style="color:{rank_colors[i+1]}">
                {rank_icons[i+1]} Rank #{i+1}
            </div>

            <h3>{row['Name']}</h3>

            📈 Completion: {round(row['Completion_Rate'],2)}% <br>
            🟢 Attendance: {row['Attendance (%)']}% <br>
            ⭐ Quality: {row['Quality_Score']} <br>
            ⏱ Deadline: {round(row['Before_Deadline_Completion (%)'],2)}% <br>
            🚀 Projects: {row['Projects_Completed']} <br>
            ⚡ Duration: {round(row['Duration_Efficiency'],2)}% <br>
            🤝 Obedience: {round(row['Obedience_Score'],2)} <br>

            <hr>
            🏆 Score: {round(row['Priority_Score'],2)} <br>
            💼 {row['Hiring_Status']}
            </div>
            """, unsafe_allow_html=True)

# -------------------------------
# 📋 DATASET (TOP 3 HIGHLIGHT + REASON)
# -------------------------------
st.subheader("📋 Dataset (Top Performers Highlighted)")

# 🔥 Recalculate TOP 3 based on FILTERED DATA (IMPORTANT)
top3_filtered = filtered_df.sort_values(by="Priority_Score", ascending=False).head(3)
top3_names = list(top3_filtered["Name"])

# -------------------------------
# 🧠 HIRING REASON LOGIC
# -------------------------------
def hiring_reason(row):
    reasons = []

    if row["Completion_Rate"] > 85:
        reasons.append("High Task Completion")

    if row["Attendance (%)"] > 90:
        reasons.append("Excellent Attendance")

    if row["Quality_Score"] > 8:
        reasons.append("High Quality Work")

    if row["Before_Deadline_Completion (%)"] > 85:
        reasons.append("Meets Deadlines Early")

    if row["Duration_Efficiency"] > 70:
        reasons.append("Fast Delivery")

    return ", ".join(reasons)

filtered_df["Hiring_Reason"] = filtered_df.apply(hiring_reason, axis=1)

# -------------------------------
# 🎯 HIGHLIGHT FUNCTION (TOP 3)
# -------------------------------
def highlight_top(row):
    if row["Name"] in top3_names:
        rank = top3_filtered[top3_filtered["Name"] == row["Name"]].index[0]
        rank_position = list(top3_filtered.index).index(rank) + 1
        color = rank_colors[rank_position]
        return [f'background-color: {color}; color: black'] * len(row)
    return [''] * len(row)

# -------------------------------
# 📊 DISPLAY TABLE
# -------------------------------
st.dataframe(
    filtered_df.style.apply(highlight_top, axis=1),
    use_container_width=True
)
# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.caption("💎 Enterprise-Level Intern Performance Intelligence Dashboard") 
