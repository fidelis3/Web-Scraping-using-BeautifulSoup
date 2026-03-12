#The information required is Average Rank, Film, and Year.
#You are required to write a Python script moviesscrape.py that extracts the information and saves it to a CSV file top_50_films.csv. You are also required to save the same information to a database Movies.db under the table name Top_50.

import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup


url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = 'top_50_films.csv'
df = pd.DataFrame(columns=["Average Rank","Film","Year"])
count = 0

html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')

#the variable tables gets the body of all the tables in the web page and the variable rows gets all the rows of the first table.
tables = data.find_all('tbody')
rows = tables[0].find_all('tr')

###SCRAPING
#The for loop iterates through each row in the rows variable, and for each row, it checks if the count variable is less than 50. If it is, it finds all the columns in the row using the find_all() method and checks if there are any columns (i.e., if len(col) != 0). If there are columns, it creates a dictionary data_dict with the Average Rank, Film, and Year extracted from the columns. Then, it creates a DataFrame df1 from the dictionary and concatenates it with the existing DataFrame df. Finally, it increments the count variable by 1. If the count variable reaches 50, the loop breaks.
for row in rows:
    if count<50:
        col = row.find_all('td')
        if len(col)!=0:
            data_dict = {"Average Rank": col[0].contents[0],
                         "Film": col[1].contents[0],
                         "Year": col[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df,df1], ignore_index=True)
            count+=1
    else:
        break
    
    
    print(df)
    
    
###SAVING TO CSV
df.to_csv(csv_path)

###SAVING TO DATABASE
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()