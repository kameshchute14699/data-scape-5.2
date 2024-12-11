import requests as rq

from bs4 import BeautifulSoup

from bs4.element import NavigableString

import pandas as pd

newsUrl ='https://www.ft.com/stream/7e37c19e-8fa3-439f-a870-b33f0520bcc0'

newsHeader = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0 Safari/537.36",
    "sec-ch-ua": '"Chromium";v="117", "Not;A=Brand";v="8", "Google Chrome";v="117"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "FTAllocation-1a93dae2-0255-4a87-8d67-c2a6912221c1; FTClientSessionId=dd44fefc"
}

    

newsResp = rq.get(url=newsUrl,headers=newsHeader)

newssoup =BeautifulSoup(newsResp.content,'html.parser')

All_news = newssoup.find_all('div',attrs={'class':'o-teaser__heading'})

for news in All_news:
    print('news',news.text)

news_headlines=[news.text for news in All_news]  

NewsDf = pd.DataFrame(news_headlines)

NewsDf.to_csv('News.csv')