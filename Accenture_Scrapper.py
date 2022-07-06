from selenium import webdriver
from bs4 import BeautifulSoup
import time

from pymongo import MongoClient
client = MongoClient("mongodb+srv://akahinternship:akahinternship@cluster0.wvqnd.mongodb.net/?retryWrites=true&w=majority")
db = client["jobs"]
collection = db["joblist"]

DRIVER_PATH = r"C:\Users\91939\Desktop\chromedriver.exe"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get("https://www.accenture.com/in-en/careers/jobsearch?src=inFY22pscgoogle&")

time.sleep(5)

soup = BeautifulSoup(driver.page_source, "html.parser")

Entire_Job = soup.find('div', class_='upper-set-jobs job-listing-block col-xs-12')

Location = Entire_Job.find_all('span', class_='corporate-semibold job-city-state')

Locations = []
for loc in Location:
    Locations.append(loc.text)


jobTitle = Entire_Job.find_all("a")

JobTitles = []
for titles in jobTitle:
    JobTitles.append(titles.text)


OverallJob = Entire_Job.find_all("span", class_ = 'areas-of-interest corporate-semibold')

OverallJobs = []
for jobs in OverallJob:
    OverallJobs.append(jobs.text)


BusinessArea = Entire_Job.find_all("p", class_ = 'job-business-area corporate-regular')

BAreas = []
for areas in BusinessArea:
    BAreas.append(areas.text)


jobLink = Entire_Job.find_all('a')

JLinks = []
for links in jobLink:
    JLinks.append(links.get("href"))


for i in range(0, len(JobTitles)):
    post = {"company":"Accenture","Job_Title": JobTitles[i], "Job_Category":OverallJobs[i], "Job_Location":Locations[i], "Job_Qualifications":"~", "Job_Link":JLinks[i]}
    collection.insert_one(post)
