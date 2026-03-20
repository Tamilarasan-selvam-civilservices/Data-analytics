## Data Preprocessing Steps

1. **Data Generation**
   - Created a synthetic dataset of 100 interns using Python (NumPy & Pandas).
   - Included features like tasks, performance, attendance, and feedback to simulate real-world intern data.

2. **Data Loading**
   - Loaded the generated dataset (`intern_performance.csv`) into a Pandas DataFrame for further processing.

3. **Data Cleaning**
   - Converted 'Start_Date' and 'End_Date' to datetime format.
   - Ensured logical consistency:
     - Tasks Completed ≤ Tasks Assigned
   - Removed duplicate records.
   - Filtered invalid values:
     - Attendance greater than 100% removed.

4. **Data Validation**
   - Checked for missing values using `.isnull()`.
   - Verified data types using `.info()`.
   - Reviewed statistical summary using `.describe()` for better understanding of data distribution.

5. **Feature Engineering**
   - Created new features:
     - **Completion Rate** = (Tasks Completed / Tasks Assigned) × 100
     - **Duration Days** = End Date – Start Date

6. **Data Storage (Load Step)**
   - Saved the processed data into Excel format for easy analysis and sharing.
   - Files generated:
     - `intern_performance.xlsx` (raw/original data)
     - `cleaned_intern_data.xlsx` (cleaned and processed data)

7. **Final Dataset**
   - Cleaned and structured dataset is ready for Exploratory Data Analysis (EDA) in the next sprint ,sprint 2

---

## About the Dataset Files

### 1. `intern_performance.csv` (Raw Data)
- This is the **original dataset** generated using Python.
- Contains unprocessed data (before cleaning).
- Used as the base input for preprocessing.

### 2. `cleaned_intern_data.csv` (Processed Data)
- This is the **cleaned and transformed dataset**.
- Generated after:
  - Data cleaning
  - Validation
  - Feature engineering
- Used for analysis, visualization, and dashboard building.

---

## Why Two Files?

- Keeping both datasets helps in:
  - Comparing raw vs cleaned data
  - Maintaining data transparency
  - Following real-world data engineering practices

👉 In real projects:
- Raw data is always preserved
- Cleaned data is used for analysis

---

## Summary

- Raw Data → `intern_performance.csv`
- Cleaned Data → `cleaned_intern_data.csv`
- Excel Files → For easy viewing and reporting

This completes the data preparation pipeline and ensures the dataset is ready for further analysis.