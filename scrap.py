from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    shub=BeautifulSoup(html_file,'lxml')

# print(shub.prettify())

""" TICS Method to parse the data as per requirement

T: tag
I: Id
C: Class
S: Selectors"""

# scrap_data= shub.div.text
# for scrap_data in shub.find_all('div',class_='article') :
#     print(scrap_data)

# for scrap_data in shub.find_all('div',class_='footer'):
#     refined_data=scrap_data.text
#     print(refined_data)


for scrap_data in shub.find_all('div',class_='article'):
    refined_data_1=scrap_data.a.text
    refined_data_2=scrap_data.p.text

    print(refined_data_1)
    
    print(refined_data_2)
    print("")