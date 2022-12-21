import requests
from lxml import html
import json
"""
Задание на странице урока отсутствует, поэтому сделал задание, о ктр говорил
преподаватель на лекции. Проанализировал новости с сайта lenta.ru
"""

url = "https://lenta.ru/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0",
}
params = {}
response = requests.get(url=url, params=params, headers=headers)
dom = html.fromstring(response.text)
news_list = dom.xpath("//body/div/div/main/div/section/div/div/div/a[contains(@class, '_topnews')]")

news_dict = dict()
for news in news_list:
    news_link = news.xpath("@href")[0]
    news_dict[url + news_link] = dict()

json_object = json.dumps(news_dict, indent=4)
with open("lentaru.json", "w") as outfile:
    outfile.write(json_object)


