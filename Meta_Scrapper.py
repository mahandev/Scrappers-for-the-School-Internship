from selenium import webdriver
from bs4 import BeautifulSoup
import time

from pymongo import MongoClient
client = MongoClient("mongodb+srv://akahinternship:akahinternship@cluster0.wvqnd.mongodb.net/?retryWrites=true&w=majority")
db = client["jobs"]
collection = db["joblist"]

DRIVER_PATH = r"C:\Users\91939\Desktop\chromedriver.exe"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get("https://www.metacareers.com/jobs")

time.sleep(5)

soup = BeautifulSoup(driver.page_source, "html.parser")

Entire_Element = soup.find("div", class_ = '_8tk7')

jobTitle = Entire_Element.find_all("div", class_='_8sel _97fe')

JobTitle = []
for titles in jobTitle:
    JobTitle.append(titles.text)

LocationCategoryOverallJob = Entire_Element.find_all("div", class_='_8see _97fe')

LocationsCategoryOverallJobs = []
for loc in LocationCategoryOverallJob:
    LocationsCategoryOverallJobs.append(loc.text)

Locations = []
Locations.append(LocationsCategoryOverallJobs[0::3])

Category = []
Category.append(LocationsCategoryOverallJobs[1::3])

OverallJob = []
OverallJob.append(LocationsCategoryOverallJobs[2::3])

URL = Entire_Element.find_all('a', class_ = '_8sef')
JURL = []
for links in URL:
    JURL.append(links.get("href"))

for i in range(0, len(JobTitle)):
    post = {"company":"Meta","Job_Title":JobTitle[i], "Job_Category":Category[0][i], "Job_Location":Locations[0][i], "Job_Qualifications":"~", "Job_Link":"metacareers.com" + JURL[i]}
    collection.insert_one(post)

driver.quit()
