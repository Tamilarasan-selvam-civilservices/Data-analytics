# 📊 Intern Performance Analytics & Insights Dashboard

## 📌 Project Objective
The goal of this project is to analyze intern performance data and generate meaningful business insights using data analytics techniques.

The project follows a structured approach:
- Data Collection & Preparation
- Exploratory Data Analysis (EDA)
- KPI Identification & Dashboard (upcoming)

---

# 🚀 Sprint 1 – Data Collection & Preparation

## Objective
To create, clean, and prepare a structured dataset for analysis.

## Steps Performed

### 1. Data Generation
- Created a synthetic dataset of 100 interns using Python (NumPy & Pandas)
- Simulated real-world intern performance data

### 2. Data Loading
- Loaded dataset (`intern_performance.csv`) into Pandas

### 3. Data Cleaning
- Converted date columns to datetime format
- Ensured:
  - Tasks Completed ≤ Tasks Assigned
- Removed duplicates
- Filtered invalid values (Attendance > 100%)

### 4. Data Validation
- Checked missing values (`.isnull()`)
- Verified data types (`.dtypes`)
- Generated statistical summary (`.describe()`)

### 5. Outlier Handling
- Used IQR method to detect outliers in Performance Score
- Removed extreme values for better analysis

### 6. Feature Engineering
- Created:
  - **Completion Rate** = (Tasks Completed / Tasks Assigned) × 100
  - **Duration Days** = End Date – Start Date

### 7. Data Storage (ETL Process)
- Raw Data → `intern_performance.csv`
- Cleaned Data → `cleaned_intern_data.csv`
- Excel Export:
  - `intern_performance.xlsx`
  - `cleaned_intern_data.xlsx`

## Output
- Clean, structured dataset ready for analysis
- Pipeline follows: **Extract → Transform → Load (ETL)**

---

# 📊 Sprint 2 – Exploratory Data Analysis (EDA)

## Objective
To analyze intern performance data and extract insights using statistical and visual techniques.

## Steps Performed

### 1. Statistical Analysis
- Used `.describe()` for summary statistics
- Calculated:
  - Average Performance Score
  - Average Completion Rate
  - Average Attendance

### 2. Data Validation
- Checked missing values
- Verified dataset consistency
- Identified outliers using IQR method

### 3. Trend Analysis
- Department-wise performance comparison
- Mentor-wise performance evaluation
- Correlation analysis between:
  - Performance Score
  - Hours Worked
  - Attendance
  - Completion Rate

### 4. Segmentation Analysis
- Top Performers (Score > 8)
- Low Performers (Score < 6)
- Compared:
  - Working hours
  - Attendance

### 5. Visualizations
Generated plots:
- Performance Distribution
- Department-wise Performance (Bar Chart)
- Hours vs Performance (Scatter Plot)
- Completion Rate Distribution
- Performance by Department (Boxplot)

All plots are stored in the `plots/` folder.

---

# 💡 Key Insights

- Higher completion rates lead to better performance.
- Attendance above 90% strongly improves outcomes.
- Certain departments show consistently higher performance.
- Mentorship plays a key role in intern success.
- Top performers work more hours and maintain higher attendance.
- Data distribution is stable with minimal outliers.

---

# 📈 Business Recommendations

- Improve task tracking to boost productivity
- Monitor attendance to identify low performers early
- Assign experienced mentors for better outcomes
- Provide training/support for low-performing interns
- Optimize workload distribution across departments

---

# 📂 Dataset Features & Justification

## Core Features

- **Intern_ID** → Unique identifier
- **Name** → Intern identity
- **Department** → Domain classification
- **Mentor** → Assigned mentor
- **Start_Date & End_Date** → Internship duration
- **Tasks_Assigned** → Workload
- **Tasks_Completed** → Productivity
- **Performance_Score** → Performance rating
- **Attendance (%)** → Consistency measure
- **Hours_Worked** → Effort indicator
- **Projects_Completed** → Practical contribution
- **Feedback_Score** → Qualitative evaluation
- **Stipend** → Compensation

---

## Derived Features

- **Completion_Rate**
  - (Tasks Completed / Tasks Assigned) × 100
  - Measures efficiency

- **Duration_Days**
  - Internship duration in days

---

## Why These Features?

These features help to:
- Measure **productivity**
- Evaluate **performance**
- Track **effort**
- Compare across departments & mentors
- Generate meaningful business insights

---

# 📁 Project Structure
intern-performance-analytics/
│
├── main.py
│ # Sprint 1: Data generation, cleaning, validation, and ETL process
│
├── eda.py
│ # Sprint 2: Exploratory Data Analysis (statistics, trends, visualizations, insights)
│
├── intern_performance.csv
│ # Raw dataset (generated data)
│
├── cleaned_intern_data.csv
│ # Cleaned and processed dataset
│
├── intern_performance.xlsx
│ # Raw dataset in Excel format (for reporting)
│
├── cleaned_intern_data.xlsx
│ # Cleaned dataset in Excel format
│
├── plots/
│ # Contains all EDA visualizations
│ ├── performance_distribution.png
│ ├── department_performance.png
│ ├── hours_vs_performance.png
│ ├── completion_rate_distribution.png
│ └── boxplot_department.png
│
├── README.md
│ # Complete project documentation

