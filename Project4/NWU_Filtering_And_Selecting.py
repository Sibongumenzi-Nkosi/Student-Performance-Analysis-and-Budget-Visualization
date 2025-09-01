#read dataframe from csv
import pandas as pd

df =pd.read_csv("grades.csv")
print(df)

df_course = df[df['Course'] =='Databases']
print(df_course)

#shows students with grade less than 40%
df_grade = df[df['Grade'] <40]
print('Grade < 40')
print(df_grade)

#Shows student with grade above 75%
df_programming = df[(df['Course'] == 'Programming') & (df['Grade'] >= 75)]
print(' Grade >75')
print( df_programming)
