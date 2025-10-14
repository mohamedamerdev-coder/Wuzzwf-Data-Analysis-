#import modules

import requests
import csv
from bs4 import BeautifulSoup
from itertools import zip_longest


job_title = []
skills = []
company_name = []
locations_name = []

# fetching the url
result = requests.get("https://wuzzuf.net/search/jobs?q=python")

# saveing page content
src = result.content
# print(src)

# createing the soup object
soup = BeautifulSoup(src, "lxml")
# print(soup)

# find the elements containing info we need
# job titles, job skills, company names, location names
job_titles = soup.find_all("h2", {"class":"css-193uk2c"} )
company_names = soup.find_all("a", {"class": "css-ipsyv7"} )
locations_names = soup.find_all("span", {"class": "css-16x61xq"} )
job_skills = soup.find_all("a", {"class": "css-5x9pm1"} )

# loop over returned lists to extract needed info into other lists

for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    company_name.append(company_names[i].text)
    skills.append(job_skills[i].text)
    locations_name.append(locations_names[i].text)


# create csv file and fill it with values
file_list = [job_title, company_name, locations_name, skills]
exported = zip_longest(*file_list)
with open("/Users/mo761/Documents/jobstest.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["job_title", "company name", "location", "skils"])
    wr.writerows(exported)
