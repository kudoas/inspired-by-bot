from bs4 import BeautifulSoup
import requests


def get_title(url: 'taget url') -> 'contents title: string':
    result = requests.get(url)
    soup = BeautifulSoup(result.content, "html.parser")
    title = str(
        soup.find('title')
    ).replace('<title>', '').replace('</title>', '')
    return title


# please refer to this repo: https://github.com/7ma7X/qiita-trend-api
def get_qiita_trend(n=10) -> list:
    res = requests.get(
        "https://qiita-api.netlify.app/.netlify/functions/trend"
    )
    try:
        res.raise_for_status()
        res_data = res.json()
        title_and_urls = []
        for i in range(n):
            url = "https://qiita.com/" + \
                res_data[i]['node']['author']["urlName"] + \
                '/items/'+res_data[i]['node']['uuid']
            title = res_data[i]['node']['title']
            title_and_urls.append((title, url))
    except requests.exceptions.RequestException as error:
        print('error', error)

    return title_and_urls
