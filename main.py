from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime

print('Put some skill that you are familiar with')
familiar_skill = input('>')
print(f'Filtering out {familiar_skill}')

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

html_text = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={familiar_skill}&txtLocation=India').text

soup =BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')

def find_jobs():
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').text.replace(' ', '')
        if 'few' in published_date:
            company_name = job.find('h3',class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span',class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/out_file.txt', 'a') as f:
                    f.write(f"{index}.) Company Name: {company_name.strip()} | Skills: {skills.strip()}  | Published: {published_date.strip()} \n")
                    f.write(f" More_info: {more_info} \n")
                    f.write("\n")
            print(f'file saved: out_file.txt')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} minutes')
        time.sleep(time_wait * 60)



