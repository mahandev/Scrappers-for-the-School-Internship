from selenium import webdriver
import time
from bs4 import BeautifulSoup

DRIVER_PATH = r"C:\Users\91939\Desktop\chromedriver.exe"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get("https://careers.microsoft.com/us/en/search-results?rt=professional")

time.sleep(5)

soup = BeautifulSoup(driver.page_source, "html.parser")

EntireElement = soup.find("ul", {"data-ph-at-id": "jobs-list"})

JobTitle = EntireElement.find_all("span", class_ = 'job-title')

JobTitles = []
for jobs in JobTitle:
    JobTitles.append(jobs.text)

JobLocation = soup.find_all("span", class_ = 'job-location')

jobLocations = []
for loc in JobLocation:
    withSpaces = loc.text
    noSpaces = withSpaces.replace(" ", "").replace("\n", "")
    jobLocations.append(noSpaces)
print(jobLocations)

jobCategory = soup.find_all("span", class_ = 'job-category')
JobCategories = []
for categories in jobCategory:
    withSpaces1 = categories.text
    noSpaces1 = withSpaces1.replace(" ", "").replace("\n", "")
    JobCategories.append(noSpaces1)
print(JobCategories)

jobLink = EntireElement.find_all("a", {"role":"link"})
jobLinks = []
for link in jobLink:
    jobLinks.append(link.get("href"))
print(jobLinks)

driver.quit()
