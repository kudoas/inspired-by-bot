from bs4 import BeautifulSoup
import requests


def get_title(url: 'taget url') -> 'contents title: string':
    result = requests.get(url)
    soup = BeautifulSoup(result.content, "html.parser")
    title = str(soup.find('title')).replace(
        '<title>', '').replace('</title>', '')
    return title


# please refer to this repo: https://github.com/7ma7X/qiita-trend-api
def get_qiita_trand_title():
    res = requests.get(
        "https://qiita-api.netlify.app/.netlify/functions/trend")
    trand = []
    for i in range(10):
        trand.append(res.json()[i]['node']['title'])
    return trand
