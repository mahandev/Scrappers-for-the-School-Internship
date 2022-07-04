from selenium import webdriver
from bs4 import BeautifulSoup

DRIVER_PATH = r"C:\Users\91939\Desktop\chromedriver.exe"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get("https://www.metacareers.com/jobs")

driver.implicitly_wait(8)

soup = BeautifulSoup(driver.page_source, "html.parser")

Entire_Element = soup.find("div", class_ = '_8tk7')

jobTitle = Entire_Element.find_all("div", class_='_8sel _97fe')

JobTitle = []
for titles in jobTitle:
    JobTitle.append(titles.text)
print(JobTitle)

LocationCategoryOverallJob = Entire_Element.find_all("div", class_='_8see _97fe')

LocationsCategoryOverallJobs = []
for loc in LocationCategoryOverallJob:
    LocationsCategoryOverallJobs.append(loc.text)
print(LocationsCategoryOverallJobs)

Locations = []
Locations.append(LocationsCategoryOverallJobs[0::3])
print(Locations)

Category = []
Category.append(LocationsCategoryOverallJobs[1::3])
print(Category)

OverallJob = []
OverallJob.append(LocationsCategoryOverallJobs[2::3])
print(OverallJob)

# This only prints the URL after "https://www.metacareers.com/jobs". Need to add this URL after the meta url in the database!
URL = Entire_Element.find_all('a', class_ = '_8sef')
JURL = []
for links in URL:
    JURL.append(links.get("href"))

