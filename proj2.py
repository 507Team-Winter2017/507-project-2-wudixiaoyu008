#proj2.py
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
url = "http://nytimes.com"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
head_title = soup.find_all(class_="story-heading")

print_title = []
for item in head_title:
    if item.a:
        print_title.append(item.a.text.replace("\n", " ").strip())
    else:
        print_title.append(item.contents[0].strip())

for title in print_title[:10]:
    print (title)


#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
url2 = "https://www.michigandaily.com/"
html2 = urllib.request.urlopen(url2, context=ctx).read()
soup2 = BeautifulSoup(html2, 'html.parser')
mostread = soup2.find(class_='pane-mostread')
li = mostread('li')
for item in li:
    print (item.text)




#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here


#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
