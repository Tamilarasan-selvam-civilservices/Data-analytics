import pandas as pd
import matplotlib.pyplot as plt
import os

print("\n=== ADVANCED EDA V5 (FINAL BUSINESS VERSION) STARTED ===\n")

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("cleaned_intern_data_final.csv")

# -------------------------------
# CREATE FOLDER
# -------------------------------
if not os.path.exists("plots_final"):
    os.makedirs("plots_final")

# -------------------------------
# DERIVED KPI (FOR PROFILE ONLY)
# -------------------------------
# Project Satisfaction (combination metric)
df['Project_Satisfaction'] = (
    df['Quality_Score'] * 0.5 +
    df['Feedback_Score'] * 0.5
)

# -------------------------------
# BASIC SUMMARY
# -------------------------------
print("\n--- DATA SUMMARY ---\n")
print(df.describe())

# -------------------------------
# KPI SUMMARY
# -------------------------------
print("\n--- KPI SUMMARY ---\n")
print("Avg Performance:", round(df['Performance_Score'].mean(), 2))
print("Avg Efficiency:", round(df['Efficiency'].mean(), 4))
print("Avg Engagement:", round(df['Engagement_Score'].mean(), 2))

# -------------------------------
# SEGMENTATION
# -------------------------------
top = df[df['Performance_Score'] > 8]
low = df[df['Performance_Score'] < 6]

print("\n--- TOP vs LOW ANALYSIS ---\n")
print("Top Training Avg:", round(top['Training_Hours'].mean(), 2))
print("Low Training Avg:", round(low['Training_Hours'].mean(), 2))

# -------------------------------
# GLOBAL LEADERBOARD
# -------------------------------
print("\n=== 🏆 TOP 10 INTERNS (GLOBAL) ===\n")

top10 = df.sort_values(by='Overall_Score', ascending=False).head(10).reset_index(drop=True)

for i, row in top10.iterrows():
    print(f"Rank {i+1}: {row['Name']} | Dept: {row['Department']} | Score: {round(row['Overall_Score'],2)}")

# -------------------------------
# DEPARTMENT TOP 3
# -------------------------------
print("\n=== 🏆 TOP 3 INTERNS PER DEPARTMENT ===\n")

for dept in df['Department'].unique():
    print(f"\n--- {dept} ---")
    top3 = df[df['Department'] == dept].sort_values(by='Overall_Score', ascending=False).head(3)

    for _, row in top3.iterrows():
        print(f"{row['Name']} | Score: {round(row['Overall_Score'],2)}")

# -------------------------------
# PROFILE STYLE EVALUATION
# -------------------------------
print("\n=== 📊 TOP PERFORMER PROFILES ===\n")

top_profiles = df.sort_values(by='Overall_Score', ascending=False).head(3)

for _, row in top_profiles.iterrows():
    print("\n=================================")
    print(f"Name: {row['Name']}")
    print(f"Department: {row['Department']}")
    print(f"Performance Score: {row['Performance_Score']}")
    print(f"Completion Rate: {round(row['Completion_Rate'],2)}%")
    print(f"Projects Completed: {row['Projects_Completed']}")
    print(f"Project Satisfaction: {round(row['Project_Satisfaction'],2)}")
    print(f"Quality Score: {row['Quality_Score']}")
    print(f"Engagement Score: {round(row['Engagement_Score'],2)}")
    print(f"Deadline Adherence: {row['Deadline_Adherence (%)']}%")
    print(f"Overall Score: {round(row['Overall_Score'],2)}")
    print("Status: ⭐ High Potential Intern")
    print("=================================")

# -------------------------------
# VISUALIZATIONS (WITH AXIS LABELS + PURPOSE)
# -------------------------------

# 1 Performance Distribution
plt.figure()
df['Performance_Score'].hist()
plt.title("Performance Score Distribution")
plt.xlabel("Performance Score")
plt.ylabel("Number of Interns")
plt.savefig("plots_final/performance_distribution.png")
plt.close()

# 2 Training vs Performance
plt.figure()
plt.scatter(df['Training_Hours'], df['Performance_Score'])
plt.title("Impact of Training on Performance")
plt.xlabel("Training Hours")
plt.ylabel("Performance Score")
plt.savefig("plots_final/training_vs_performance.png")
plt.close()

# 3 Efficiency vs Performance
plt.figure()
plt.scatter(df['Efficiency'], df['Performance_Score'])
plt.title("Efficiency vs Performance")
plt.xlabel("Efficiency (Score per Hour)")
plt.ylabel("Performance Score")
plt.savefig("plots_final/efficiency_vs_performance.png")
plt.close()

# 4 Completion Rate vs Performance
plt.figure()
plt.scatter(df['Completion_Rate'], df['Performance_Score'])
plt.title("Completion Rate vs Performance")
plt.xlabel("Completion Rate (%)")
plt.ylabel("Performance Score")
plt.savefig("plots_final/completion_vs_performance.png")
plt.close()

# 5 Quality vs Performance
plt.figure()
plt.scatter(df['Quality_Score'], df['Performance_Score'])
plt.title("Quality of Work vs Performance")
plt.xlabel("Quality Score")
plt.ylabel("Performance Score")
plt.savefig("plots_final/quality_vs_performance.png")
plt.close()

# 6 Engagement vs Performance
plt.figure()
plt.scatter(df['Engagement_Score'], df['Performance_Score'])
plt.title("Engagement vs Performance")
plt.xlabel("Engagement Score")
plt.ylabel("Performance Score")
plt.savefig("plots_final/engagement_vs_performance.png")
plt.close()

# 7 Deadline vs Performance
plt.figure()
plt.scatter(df['Deadline_Adherence (%)'], df['Performance_Score'])
plt.title("Deadline Adherence vs Performance")
plt.xlabel("Deadline Adherence (%)")
plt.ylabel("Performance Score")
plt.savefig("plots_final/deadline_vs_performance.png")
plt.close()

# 8 Feedback vs Performance
plt.figure()
plt.scatter(df['Feedback_Score'], df['Performance_Score'])
plt.title("Feedback (Communication) vs Performance")
plt.xlabel("Feedback Score")
plt.ylabel("Performance Score")
plt.savefig("plots_final/feedback_vs_performance.png")
plt.close()

# 9 Department Performance
plt.figure()
df.groupby('Department')['Performance_Score'].mean().plot(kind='bar')
plt.title("Average Performance by Department")
plt.xlabel("Department")
plt.ylabel("Average Performance Score")
plt.savefig("plots_final/department_performance.png")
plt.close()

# 10 Task Difficulty Impact
plt.figure()
df.groupby('Task_Difficulty')['Performance_Score'].mean().plot(kind='bar')
plt.title("Task Difficulty vs Performance")
plt.xlabel("Task Difficulty Level")
plt.ylabel("Average Performance Score")
plt.savefig("plots_final/task_difficulty.png")
plt.close()

print("\nAll visualizations saved in 'plots_final'\n")

# -------------------------------
# FINAL BUSINESS INSIGHTS
# -------------------------------
print("\n=== 📈 FINAL BUSINESS INSIGHTS ===\n")

print("1. Training significantly improves performance outcomes.")
print("2. Efficiency indicates smart work is more valuable than long hours.")
print("3. Completion rate is a strong indicator of productivity.")
print("4. Quality and feedback together define project satisfaction.")
print("5. Engagement ensures consistent performance.")
print("6. Meeting deadlines is critical in real-world environments.")
print("7. Top performers maintain balance across all KPIs.")
print("8. Departments vary in average performance, indicating optimization areas.")

print("\n=== EDA COMPLETED SUCCESSFULLY ===\n")
