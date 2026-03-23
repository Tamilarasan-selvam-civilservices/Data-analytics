import pandas as pd
import numpy as np

# -------------------------------
# STEP 1: DATA GENERATION
# -------------------------------

print("\n--- Generating Dataset ---\n")

np.random.seed(1)
n = 100

df = pd.DataFrame({
    "Intern_ID": range(1, n+1),
    "Name": ["Intern_" + str(i) for i in range(1, n+1)],
    "Department": np.random.choice(["Data Science", "Marketing", "HR"], n),
    "Mentor": np.random.choice(["Mentor_A", "Mentor_B", "Mentor_C"], n),
    "Start_Date": pd.date_range(start="2025-01-01", periods=n),
    "End_Date": pd.date_range(start="2025-04-01", periods=n),
    "Tasks_Assigned": np.random.randint(40, 100, n),
    "Tasks_Completed": np.random.randint(20, 100, n),
    "Performance_Score": np.round(np.random.uniform(6, 10, n), 2),
    "Attendance (%)": np.round(np.random.uniform(75, 100, n), 2),
    "Hours_Worked": np.random.randint(150, 300, n),
    "Projects_Completed": np.random.randint(2, 8, n),
    "Feedback_Score": np.round(np.random.uniform(3, 5, n), 2),
    "Stipend": np.random.randint(8000, 20000, n)
})

df.to_csv("intern_performance.csv", index=False)
print("Raw dataset created\n")

# -------------------------------
# STEP 2: LOAD DATA
# -------------------------------

df = pd.read_csv("intern_performance.csv")
print("Dataset loaded\n")

# -------------------------------
# STEP 3: DATA CLEANING
# -------------------------------

print("\n--- Cleaning Data ---\n")

# Convert date columns
df['Start_Date'] = pd.to_datetime(df['Start_Date'])
df['End_Date'] = pd.to_datetime(df['End_Date'])

# Logical consistency
df['Tasks_Completed'] = np.minimum(df['Tasks_Completed'], df['Tasks_Assigned'])

# Remove duplicates
df.drop_duplicates(inplace=True)

# Filter invalid attendance
df = df[df['Attendance (%)'] <= 100]

print("Basic cleaning done\n")

# -------------------------------
# STEP 4: DATA VALIDATION
# -------------------------------

print("\n--- Data Validation ---\n")

# Missing values check
print("Missing Values:\n", df.isnull().sum())

# Data types
print("\nData Types:\n")
print(df.dtypes)

# Statistical summary
print("\nStatistical Summary:\n")
print(df.describe())

# -------------------------------
# STEP 5: OUTLIER HANDLING (NEW 🔥)
# -------------------------------

Q1 = df['Performance_Score'].quantile(0.25)
Q3 = df['Performance_Score'].quantile(0.75)
IQR = Q3 - Q1

df = df[(df['Performance_Score'] >= Q1 - 1.5 * IQR) &
        (df['Performance_Score'] <= Q3 + 1.5 * IQR)]

print("\nOutliers removed based on Performance Score\n")

# -------------------------------
# STEP 6: FEATURE ENGINEERING
# -------------------------------

print("\n--- Feature Engineering ---\n")

df['Completion_Rate'] = (df['Tasks_Completed'] / df['Tasks_Assigned']) * 100
df['Duration_Days'] = (df['End_Date'] - df['Start_Date']).dt.days

print("New features created\n")

# -------------------------------
# STEP 7: SAVE CLEANED DATA
# -------------------------------

df.to_csv("cleaned_intern_data.csv", index=False)
print("Cleaned dataset saved\n")

# -------------------------------
# STEP 8: LOAD TO EXCEL (ETL STEP)
# -------------------------------

pd.read_csv("intern_performance.csv").to_excel("intern_performance.xlsx", index=False)
df.to_excel("cleaned_intern_data.xlsx", index=False)

print("Data exported to Excel\n")

# -------------------------------
# FINAL OUTPUT
# -------------------------------

print("\nFinal dataset preview:\n")
print(df.head())

print("\nSprint 1 Completed Successfully  🚀\n")
