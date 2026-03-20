## Dataset Features & Justification

The dataset includes multiple features to evaluate intern performance from different perspectives:

1. **Intern_ID**
   - Unique identifier for each intern
   - Helps in tracking and referencing records

2. **Name**
   - Represents intern identity (for readability)

3. **Department**
   - Shows which domain the intern belongs to (Data Science, Marketing, HR)
   - Useful for comparing performance across departments

4. **Mentor**
   - Indicates the assigned mentor
   - Helps analyze mentor-wise performance trends

5. **Start_Date & End_Date**
   - Defines internship duration
   - Used to calculate total working period

6. **Tasks_Assigned**
   - Total number of tasks given
   - Represents workload

7. **Tasks_Completed**
   - Number of tasks completed by intern
   - Used to evaluate productivity

8. **Performance_Score**
   - Overall rating (1–10)
   - Direct indicator of intern performance

9. **Attendance (%)**
   - Measures presence and consistency
   - Important factor in performance evaluation

10. **Hours_Worked**
    - Total hours contributed
    - Helps measure effort level

11. **Projects_Completed**
    - Number of projects completed
    - Indicates practical contribution

12. **Feedback_Score**
    - Mentor’s rating (1–5)
    - Reflects qualitative performance

13. **Stipend**
    - Monthly compensation
    - Can be analyzed against performance


### Derived Features (Created During Preprocessing)

14. **Completion_Rate**
   - Calculated as: (Tasks Completed / Tasks Assigned) × 100
   - Helps understand efficiency

15. **Duration_Days**
   - Internship duration in days
   - Useful for time-based analysis



### Why These Features?

These features were selected to:
- Capture **productivity** (tasks, projects)
- Measure **performance** (scores, feedback)
- Track **effort** (hours worked, attendance)
- Enable **comparative analysis** (department, mentor)
- Support **business insights** in later stages (EDA & dashboard)
