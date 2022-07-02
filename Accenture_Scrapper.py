from selenium import webdriver
import time
from bs4 import BeautifulSoup

DRIVER_PATH = r"C:\Users\91939\Desktop\chromedriver.exe"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get("https://www.accenture.com/in-en/careers/jobsearch?src=inFY22pscgoogle&")

# time.sleep(5)
driver.implicitly_wait(8)a

soup = BeautifulSoup(driver.page_source, "html.parser")

Entire_Element = soup.find('div', class_='module job-card-wrapper col-md-12 col-xs-12 col-sm-12 corporate-regular background-white list-view')

Location = Entire_Element.find("div", class_='row').text

jobTitle = Entire_Element.find("a").text

OverallJob = Entire_Element.find("span", class_ = 'areas-of-interest corporate-semibold').text

BusinessArea = Entire_Element.find("p", class_ = 'job-business-area corporate-regular').text

jobLink = Entire_Element.a['href']

print(jobLink)
print(Location)
print(jobTitle)
print(OverallJob)
print(BusinessArea)
