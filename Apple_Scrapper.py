# Imported for getting page source.
from selenium import webdriver
#Imported for adding buffer time for the program to load.
import time
# Imported for parsing and finding appropriate data in page source.
from bs4 import BeautifulSoup

links = []


# Where chromedrive is located, has to be installed for web scraping.
DRIVER_PATH = "C:\\Users\\Dev\\Desktop\\chromedriver.exe"

# Declaring the webdriver to be used in chrome.
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

#fethcing the website using the driver.
driver.get("https://jobs.apple.com/en-in/search?location=india-INDC&page=2")

#waiting for the page to load completey, this is a way to keep any internet realted issues out of the way.
time.sleep(5)
#Parsing the page source in a HTML format that bs4 understands.
soup = BeautifulSoup(driver.page_source, "html.parser")

#Getting the parent element of the element we are interested in.
job_element = soup.find("table", class_="table")

#Getting the child element out of the table this will give us a list.
job_name = job_element.find_all('a', {"class":"table--advanced-search__title"})
job_cat = job_element.find_all('span', {"class":"table--advanced-search__role"})
job_location = job_element.find_all('td', {"class":"table-col-2"})










#looping through all child elements to get indiviusal data sets.


undistributedTitles = []
distributedTitles = []
undistributedCats = []
distributedCats = []
undistributedLinks = []
distributedLinks = []
undistributedLoc = []
distributedLoc = []


for name in job_name:
    undistributedTitles.append(name.text)


for name in undistributedTitles:
    distributedTitles.append((name.replace(' ','')).replace('\n',''))


for cate in job_cat:
    undistributedCats.append(cate.text)

    
for cate in undistributedCats:
    distributedCats.append((cate.replace(' ','')).replace('\n',''))

for location in job_location:
    undistributedLoc.append(location.text)

    
for location in undistributedLoc:
    distributedLoc.append(location)


for links in job_name:
    undistributedLinks.append(links.get("href"))

for links in undistributedLinks:
    distributedLinks.append((links.replace('\n','')))

print(distributedTitles)
print(distributedCats)
print(distributedLoc)
print(distributedLinks)
driver.quit()
