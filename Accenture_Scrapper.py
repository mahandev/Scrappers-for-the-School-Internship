from selenium import webdriver
from bs4 import BeautifulSoup

DRIVER_PATH = r"C:\Users\91939\Desktop\chromedriver.exe"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get("https://www.accenture.com/in-en/careers/jobsearch?src=inFY22pscgoogle&")

driver.implicitly_wait(8)

soup = BeautifulSoup(driver.page_source, "html.parser")

Entire_Job = soup.find('div', class_='upper-set-jobs job-listing-block col-xs-12')

Location = Entire_Job.find_all('span', class_='corporate-semibold job-city-state')

Locations = []
for loc in Location:
    Locations.append(loc.text)

print(Locations)

jobTitle = Entire_Job.find_all("a")

JobTitles = []
for titles in jobTitle:
    JobTitles.append(titles.text)

print(JobTitles)

OverallJob = Entire_Job.find_all("span", class_ = 'areas-of-interest corporate-semibold')

OverallJobs = []
for jobs in OverallJob:
    OverallJobs.append(jobs.text)

print(OverallJobs)

BusinessArea = Entire_Job.find_all("p", class_ = 'job-business-area corporate-regular')

BAreas = []
for areas in BusinessArea:
    BAreas.append(areas.text)

print(BAreas)

jobLink = Entire_Job.find_all('a')

JLinks = []
for links in jobLink:
    JLinks.append(links.get("href"))

print(JLinks)
