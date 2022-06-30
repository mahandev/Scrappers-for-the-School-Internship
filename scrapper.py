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
driver.get("https://www.tesla.com/careers/search/?country=any")

#waiting for the page to load completey, this is a way to keep any internet realted issues out of the way.
time.sleep(5)
#Parsing the page source in a HTML format that bs4 understands.
soup = BeautifulSoup(driver.page_source, "html.parser")

#Getting the parent element of the element we are interested in.
job_element = soup.find("table")

#Getting the child element out of the table this will give us a list.
job_profiles = job_element.find_all('td')

link_profiles = job_element.find_all('a')

#looping through all child elements to get indiviusal data sets.



undistributedJobs = []
for job in job_profiles:
    undistributedJobs.append(job.text)
    
for link in link_profiles:
    links.append(link.get("href"))


print(undistributedJobs)
print(len(undistributedJobs))

# Yield successive n-sized
# chunks from l.
def divide_chunks(l, n):
      
    # looping till length l
    for i in range(0, len(l), n): 
        yield l[i:i + n]
  
# How many elements each
# list should have
n = 3

# Dividing and sorting jobs approprately
allJobsSorted = list(divide_chunks(undistributedJobs, n))
print (allJobsSorted)
print(links)
driver.quit()
