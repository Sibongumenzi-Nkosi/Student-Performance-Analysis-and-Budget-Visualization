import pandas as pd

#Read the CSV file into a Pandas DataFrame
df = pd.read_csv('grades.csv')

#Group the data by the 'Course' column and calculate the average grades for each course
average_grades = df.groupby('Course').agg({'Grade': 'mean'})

#print the reasulting agregated DataFrame
print(average_grades)
