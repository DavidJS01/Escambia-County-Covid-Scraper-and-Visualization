import plotly.express as px
import pandas as pd 
import mysql.connector

#Read Florida Dept. of Health CSV File Using Pandas, placing it into a dataframe
df = pd.read_csv('Florida_COVID19_Case_Line_Data (1).csv')
escambia_data = (df[df.County == 'Escambia'])
escambia_covid = escambia_data.where((pd.notnull(escambia_data)), None)

#Create CSV file from dataframe, showing all Escambia county covid information
escambia_covid.to_csv('escambia_covid.csv', index = False)

florida_database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password"

)

cursor = florida_database.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS florida_database")
cursor.execute("USE florida_database")
cursor.execute("DROP TABLE IF EXISTS florida_covid")
cursor.execute("CREATE TABLE IF NOT EXISTS florida_covid (County VARCHAR(20), Age INT, Age_group VARCHAR(20), Gender VARCHAR(20), Hospitalized VARCHAR(20), Case1 VARCHAR(100), EventDate TEXT, ID int AUTO_INCREMENT PRIMARY KEY)")
for index, row in escambia_covid.iterrows():
    cursor.execute("INSERT INTO florida_covid (County, Age, Age_group, Hospitalized, Gender, Case1, EventDate) values(%s,%s,%s,%s,%s,%s,%s)", (row.County, row.Age, row.Age_group,  row.Hospitalized, row.Gender, row.Case1, row.EventDate))

florida_database.commit()


#Return each Age_group row with its associated total number of infections
cursor.execute("SELECT Age_group, COUNT(*) as count FROM florida_covid GROUP BY Age_group ORDER BY count DESC")
age_group_result = cursor.fetchall()


#Iterate through all rows, returning each Age_group row and count of infections into a list
infected_age_groups = []
infections_by_age_group = []
for x in age_group_result:
    infected_age_groups.append(x[0])
    infections_by_age_group.append(x[1])

#Sort data into a dataframe 
chart_data = {'Age Group': infected_age_groups, 'Infections': infections_by_age_group}
df = pd.DataFrame(chart_data, columns=['Age Group', 'Infections'])

#Pass dataframe into plotly bar fuction, creating a bar graph
fig = px.bar(df, x = "Age Group", y = "Infections", title="Escambia County Total Infections by Age Group")
print(fig.show())
cursor.close()
