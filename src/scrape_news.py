from bs4 import BeautifulSoup
from urllib.request import urlopen
from store_news import replace_news_csv
from email_news import send_news_notification
import os
import pandas as pd

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
NEWS_FILE = 'news.csv'

def scrape_latest_news(stock_code):
    page_url = f"https://www.bnnbloomberg.ca/stock/{stock_code}#/News"
    
    #----------capture latest news post----------#
    page = urlopen(page_url)
    soup = BeautifulSoup(page, 'html.parser')
    news = soup.find("li", {"class": "0 feed-item index-1"})

    #----------capture news content----------#
    article_content = news.find("div",{"class": "article-content"})
    title = article_content.find('h3').text
    url = article_content.a.get('href')

    #----------capture article date----------#
    date = news.find("div",{"class": "date"}).text.strip()

    #----------capture article category----------#
    article_category = news.find("li",{"class": "highlighted"})
    category = article_category.find('h4').text

    return date, title, url, category

def compare_url(t1,t2):
    return t1[3] == t2[3]

def main():
    update_count = 0

    #load news file from csv
    df = pd.read_csv(f"{ROOT_DIR}/{NEWS_FILE}",sep='\|', engine='python', encoding='utf-8')

    #iterate through df rows
    for index, row in df.iterrows():
        #----------scrape BNNBloomberg stock for latest news----------#
        stock = row['Stock']
        latest_news_tuple = scrape_latest_news(stock)
        latest_news_tuple = (stock,) + latest_news_tuple #add stock to tuple
        previous_news_tuple = tuple(row)
        
        #----------check if news has changed----------#
        if not compare_url(latest_news_tuple,previous_news_tuple):
            print(f"stock: {stock} news has been released!")
            
            #----------send email of news update----------#
            send_news_notification(latest_news_tuple)

            #----------replace dataframe with updated news----------#
            df.loc[index]=latest_news_tuple
            update_count+=1

    #if a change in latest news occured
    if update_count>=1:        
        #----------replace news csv----------#
        replace_news_csv(df)
    else:
        print("no stock news has been released")

if __name__ == "__main__":
    main()