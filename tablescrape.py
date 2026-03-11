from bs4 import BeautifulSoup


with open('table.html','r') as file:
    content=file.read()
    
table_bs=BeautifulSoup(content,'html.parser')
print(table_bs.prettify())

table_rows=table_bs.find_all('tr')
print(table_rows )

first_row =table_rows[0]
print(first_row)

#To get child
child=first_row.find_all('td')
print(child)