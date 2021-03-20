# Escambia County COVID Statistics Scraper

This project uses the Pandas library to scrape all Escambia County COVID-19 stats from an excel file published by the Florida Department of Health.

## Installation
1. Download the repository
2. Change Directory to the Repository

Then run: 
> mysql < florida_covid_stats.sql


## Usage

This project scrapes through the Florida Department of Health Excel spreadsheet, creating a CSV file that includes all instances of Escambia county.

![image](https://user-images.githubusercontent.com/53328559/111859728-2fce8100-8900-11eb-8307-323ff6ceac6f.png)

![image](https://user-images.githubusercontent.com/53328559/111859738-3bba4300-8900-11eb-835a-27664e3c52c3.png)


Then, it creates a local MySQL database, inserting each instance of Escambia COVID-19 information from the spreadsheet into the local database.

![image](https://user-images.githubusercontent.com/53328559/111859779-8a67dd00-8900-11eb-9e27-9755576a2270.png)


![image](https://user-images.githubusercontent.com/53328559/111854536-e9b3f600-88dc-11eb-8faf-b0101ca123b8.png)

![image](https://user-images.githubusercontent.com/53328559/111855623-313d8080-88e3-11eb-8041-cf9e9f1e945b.png)


Using SQL, the project filters through the database, returning each age group with the corresponding amount of infections in descending order.

![image](https://user-images.githubusercontent.com/53328559/111854740-1583ab80-88de-11eb-8f15-eac94c1e0fad.png)

## Visualizations

The project uses the Plotly library to create a graph visualizing each age group with the corresponding amount of infections: 

![image](https://user-images.githubusercontent.com/53328559/111859800-b08d7d00-8900-11eb-8fac-68d31a7e7adb.png)


![image](https://user-images.githubusercontent.com/53328559/111854823-8f1b9980-88de-11eb-98fe-b4201223e01e.png)

![image](https://user-images.githubusercontent.com/53328559/111855695-998c6200-88e3-11eb-8a79-134fbf09d161.png)


Using the Escambia-exclusive CSV file created from the Florida Department of Health, here is an excel visualization that compares total case infections by gender:

![image](https://user-images.githubusercontent.com/53328559/111855686-8bd6dc80-88e3-11eb-87b0-96aff525e0c9.png)

## Other Visualizations

To view other visualizations, please visit my [Tableau Public Profile](https://public.tableau.com/profile/david6095#!/).
