import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
print(df)

# Filter rows where Age > 25
print(df[df['Age'] > 25])

"""
Load employee data from a dictionary, calculate the average salary, 
and filter employees with salary above average.
"""
import pandas as pd
# Create a Pandas DataFrame
data = {
    'Employee_ID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Salary': [5000, 7000, 6000, 8000]
}
df = pd.DataFrame(data)
print("Employee Data:")
print(df)
# Calculate the average salary
average_salary = df['Salary'].mean()
print("\nAverage Salary:", average_salary)
# Filter employees with salary above the average
high_salary_employees = df[df['Salary'] > average_salary]
print("\nEmployees with Salary Above Average:")
print(high_salary_employees)

"""
Python script that reads an Excel file containing employee table 
data and uses Matplotlib to create a chart. 
The example assumes the employee table 
contains columns such as Employee_ID, Department, and Salary
"""
import pandas as pd
import matplotlib.pyplot as plt
# Step 1: Load the Excel file
# Replace 'employee_data.xlsx' with the path to your Excel file
file_path = 'employee_data.xlsx'
# Read the Excel file into a pandas DataFrame
# Assumes the Excel file has a sheet with columns 'Employee_ID', 'Department', and 'Salary'
employee_data = pd.read_excel(file_path)
# Step 2: Data Preparation
# Group the data by department and calculate the total salary per department
department_salary = employee_data.groupby('Department')['Salary'].sum()
# Extract department names and total salaries for plotting
departments = department_salary.index
total_salaries = department_salary.values
# Step 3: Create the Bar Chart
plt.figure(figsize=(10, 6))  # Set the figure size
# Create a bar chart for total salary by department
plt.bar(departments, total_salaries, color='skyblue')
# Step 4: Add Chart Details
plt.title('Total Salary by Department', fontsize=16)  # Add a title
plt.xlabel('Department', fontsize=14)  # Label for the x-axis
plt.ylabel('Total Salary', fontsize=14)  # Label for the y-axis
plt.xticks(rotation=45, fontsize=12)  # Rotate x-axis labels for better visibility
plt.yticks(fontsize=12)
# Add annotations for each bar
for index, value in enumerate(total_salaries):
    plt.text(index, value + 1000, f'{value}', ha='center', fontsize=10)
# Step 5: Show the Chart
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()



