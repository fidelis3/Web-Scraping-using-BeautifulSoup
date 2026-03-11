
#Beautiful Soup is a Python library for pulling data out of HTML and XML files, we will focus on HTML files
import html

from bs4 import BeautifulSoup
import requests
#To read the content of an HTML file, we can use the open() function to read the file and then pass the content to BeautifulSoup for parsing. Here's an example of how to do this:
with open("salary.html", "r") as file:
    content = file.read()
soup = BeautifulSoup(content, 'html.parser')

#We  use the method prettify() to display the HTML in the nested structure:
print(soup.prettify())

tag_object=soup.title
print(tag_object)

#There are many H3's in the html file but when you call it you get the first one only, to get all the H3's you can use the find_all() method:
tag_object1=soup.h3
print(tag_object1)

#To get the child tag of the h3 tag, we can use the .b attribute to access the <b> tag that is a child of the <h3> tag. Here's how you can do it:
tag_child =tag_object1.b
print(tag_child)

parent_tag=tag_child.parent
print(parent_tag)


tag_object2=soup.find_all("h3")
print(tag_object2)

tag_object3 = tag_object1.find_next_sibling()
print(tag_object3)


