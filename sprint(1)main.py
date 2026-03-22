import pandas as pd
import numpy as np



# Data Preprocessing Steps


# Step 1: Created a sample dataset of interns using random values
# (since no real dataset was given, this is just for practice/analysis)

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

# saving the dataset to csv file
df.to_csv("intern_performance.csv", index=False)
print("Dataset created\n")


# Step 2: Loading the dataset into dataframe
df = pd.read_csv("intern_performance.csv")
print("Dataset loaded\n")


# Step 3: Cleaning the data

df['Start_Date'] = pd.to_datetime(df['Start_Date'])
df['End_Date'] = pd.to_datetime(df['End_Date'])
df['Tasks_Completed'] = np.minimum(df['Tasks_Completed'], df['Tasks_Assigned'])
# removing duplicate rows if present
df.drop_duplicates(inplace=True)
# removing invalid attendance values (>100)
df = df[df['Attendance (%)'] <= 100]
print("Data cleaning done\n")


# Step 4: Checking the data

print("Missing values:\n")
print(df.isnull().sum())
# checking data types and info
print("\nDataset info:\n")
print(df.info())

# statistical summary (added this — good for understanding data distribution)
print("\nStatistical Summary:\n")
print(df.describe())

# Step 5: Creating new features
df['Completion_Rate'] = (df['Tasks_Completed'] / df['Tasks_Assigned']) * 100
df['Duration_Days'] = (df['End_Date'] - df['Start_Date']).dt.days
print("\nFeature engineering done\n")
# Final dataset preview
print("Final dataset:\n")
print(df.head())


# saving cleaned dataset (optional but for only good practice)
df.to_csv("cleaned_intern_data.csv", index=False)
print("\nCleaned dataset saved")


# LOAD STEP (Saving to Excel)

# IT RESONATES THE ETL PIPELINES 
# saving raw data to excel
pd.read_csv("intern_performance.csv").to_excel("intern_performance.xlsx", index=False)

# saving cleaned data to excel
df.to_excel("cleaned_intern_data.xlsx", index=False)

print("Data loaded into Excel files successfully")
