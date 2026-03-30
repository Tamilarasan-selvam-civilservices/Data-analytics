import pandas as pd
import numpy as np

print("\n=== INTERN ANALYTICS PIPELINE (FINAL VERSION) STARTED ===\n")

# -------------------------------
# CONFIGURATION
# -------------------------------
CONFIG = {
    "num_records": 300,
    "departments": ["Data Science", "Marketing", "HR", "Finance", "Operations"],
    "mentors": ["Mentor_A", "Mentor_B", "Mentor_C", "Mentor_D"]
}

np.random.seed(42)

# -------------------------------
# DATA GENERATION
# -------------------------------
df = pd.DataFrame({
    "Intern_ID": range(1, CONFIG["num_records"] + 1),
    "Name": [f"Intern_{i}" for i in range(1, CONFIG["num_records"] + 1)],

    "Department": np.random.choice(CONFIG["departments"], CONFIG["num_records"]),
    "Mentor": np.random.choice(CONFIG["mentors"], CONFIG["num_records"]),

    "Start_Date": pd.date_range("2025-01-01", periods=CONFIG["num_records"]),
    "End_Date": pd.date_range("2025-04-01", periods=CONFIG["num_records"]),

    "Tasks_Assigned": np.random.randint(50, 130, CONFIG["num_records"]),
    "Tasks_Completed": np.random.randint(30, 130, CONFIG["num_records"]),

    "Performance_Score": np.round(np.random.uniform(5, 10, CONFIG["num_records"]), 2),
    "Attendance (%)": np.round(np.random.uniform(70, 100, CONFIG["num_records"]), 2),

    "Hours_Worked": np.random.randint(120, 320, CONFIG["num_records"]),
    "Projects_Completed": np.random.randint(1, 10, CONFIG["num_records"]),

    "Feedback_Score": np.round(np.random.uniform(2.5, 5, CONFIG["num_records"]), 2),
    "Stipend": np.random.randint(8000, 25000, CONFIG["num_records"])
})

# -------------------------------
# ADVANCED (CRITICAL ONLY)
# -------------------------------
df["Task_Difficulty"] = np.random.choice(["Easy", "Medium", "Hard"], CONFIG["num_records"])
df["Training_Hours"] = np.random.randint(10, 80, CONFIG["num_records"])
df["Overtime_Hours"] = np.random.randint(0, 60, CONFIG["num_records"])

df["Quality_Score"] = np.round(np.random.uniform(5, 10, CONFIG["num_records"]), 2)
df["Deadline_Adherence (%)"] = np.round(np.random.uniform(60, 100, CONFIG["num_records"]), 2)

df["Team_Contribution_Score"] = np.round(np.random.uniform(5, 10, CONFIG["num_records"]), 2)
df["Peer_Review_Score"] = np.round(np.random.uniform(5, 10, CONFIG["num_records"]), 2)

print("Dataset created\n")

# -------------------------------
# CLEANING
# -------------------------------
df['Start_Date'] = pd.to_datetime(df['Start_Date'])
df['End_Date'] = pd.to_datetime(df['End_Date'])

df['Tasks_Completed'] = np.minimum(df['Tasks_Completed'], df['Tasks_Assigned'])
df = df[df['Attendance (%)'] <= 100]
df.drop_duplicates(inplace=True)

print("Cleaning done\n")

# -------------------------------
# FEATURE ENGINEERING
# -------------------------------
df['Completion_Rate'] = (df['Tasks_Completed'] / df['Tasks_Assigned']) * 100
df['Duration_Days'] = (df['End_Date'] - df['Start_Date']).dt.days

df['Efficiency'] = df['Performance_Score'] / df['Hours_Worked']
df['Productivity_Index'] = df['Tasks_Completed'] + df['Projects_Completed']
df['Engagement_Score'] = (df['Attendance (%)'] + df['Feedback_Score'] * 20) / 2

df['Overall_Score'] = (
    df['Performance_Score'] * 0.4 +
    df['Quality_Score'] * 0.2 +
    df['Team_Contribution_Score'] * 0.2 +
    df['Peer_Review_Score'] * 0.2
)

print("Feature engineering done\n")

# -------------------------------
# OUTLIER HANDLING
# -------------------------------
Q1 = df['Performance_Score'].quantile(0.25)
Q3 = df['Performance_Score'].quantile(0.75)
IQR = Q3 - Q1

df = df[
    (df['Performance_Score'] >= Q1 - 1.5 * IQR) &
    (df['Performance_Score'] <= Q3 + 1.5 * IQR)
]

print("Outliers removed\n")

# -------------------------------
# SAVE
# -------------------------------
df.to_csv("cleaned_intern_data_final.csv", index=False)
df.to_excel("cleaned_intern_data_final.xlsx", index=False)

print("\n=== PIPELINE COMPLETED ===\n")
print(df.head())
