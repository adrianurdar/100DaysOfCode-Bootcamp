import requests
from bs4 import BeautifulSoup
import pandas as pd

all_majors = []
all_early_career_salaries = []
all_mid_career_salaries = []


# Go through all 34 pages from PayScale
for i in range(1, 35):
    res = requests.get(url=f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{i}")
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")

    # From each page get all the majors, early career pay, mid career pay
    # GET ALL MAJORS AND NUMBERS ON THE PAGE
    majors_data = soup.select(".csr-col--school-name .data-table__value")
    all_numbers_data = soup.select(".csr-col--right")

    # TRANSFORM THE DATA INTO 2 LISTS
    majors = [major.get_text() for major in majors_data]
    all_numbers = [number.get_text() for number in all_numbers_data]

    # CREATE A CLEAN EARLY CAREER SALARIES LIST
    early_career_salaries = [pay for pay in all_numbers if 'Early Career' in pay]
    early_career_salaries.pop(0)
    early_career_salaries = [int(salary.split('$')[1].replace(',', '')) for salary in early_career_salaries]

    # CREATE A CLEAN MID CAREER SALARIES LIST
    mid_career_salaries = [pay for pay in all_numbers if 'Mid-Career' in pay]
    mid_career_salaries.pop(0)
    mid_career_salaries = [int(salary.split('$')[1].replace(',', '')) for salary in mid_career_salaries]

    # APPEND THE SCRAPED INFO TO THE FINAL LIST
    all_majors += majors
    all_early_career_salaries += early_career_salaries
    all_mid_career_salaries += mid_career_salaries

# ADD COLUMN NAMES
all_majors.insert(0, "Major")
all_early_career_salaries.insert(0, "Early Career Pay")
all_mid_career_salaries.insert(0, "Mid-Career Pay")

df = pd.DataFrame(list(zip(all_majors, all_early_career_salaries, all_mid_career_salaries)))
print(df)

df.to_csv("highest_paying_jobs.csv", index=False)
