import requests
from bs4 import BeautifulSoup as bs
import fake_useragent
import time
import json

MAX_PAGES = 40


def get_link(text):
    user_agent = fake_useragent.UserAgent()
    data = requests.get(
        url=f"https://hh.ru/search/vacancy?text={text}&area=1&page=1",
        headers={"user-agent": user_agent.random}
    )
    if data.status_code != 200:
        return
    for page in range(MAX_PAGES):
        try:
            data = requests.get(
                url=f"https://hh.ru/search/vacancy?text={text}&area=1&page={page}",
                headers={"user-agent": user_agent.random}
            )
            if data.status_code != 200:
                continue
            soup = bs(data.content, "lxml")
            for link in soup.find_all("a", attrs={"class": "serp-item__title"}):
                yield f"{link.attrs['href']}"
        except Exception as e:
            print(f"{e}")
        time.sleep(1)


def get_vacancy(link):
    user_agent = fake_useragent.UserAgent()
    data = requests.get(
        url=link,
        headers={"user-agent": user_agent.random}
    )
    if data.status_code != 200:
        return
    soup = bs(data.content, "lxml")
    try:
        name = " ".join(soup.find(attrs={"class": "bloko-header-section-1"}))
    except:
        name = ""
    try:
        salary = soup.find(attrs={"class": "bloko-header-section-2 bloko-header-section-2_lite"}).text.replace("\xa0", "")
    except:
        salary = ""
    vacancy = {
        "name": name,
        "salary": salary,
    }
    return vacancy


for a in get_link("python junior"):
    print(get_vacancy(a))
    time.sleep(1)
