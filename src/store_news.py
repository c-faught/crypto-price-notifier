import pandas as pd
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
NEWS_FILE = 'news.csv'

def replace_news_csv(dataframe):
    dataframe.to_csv(f"{ROOT_DIR}/{NEWS_FILE}", index=False,sep='|')
    return True

def add_stock_to_news(stock):
    #load news file from csv
    df = pd.read_csv(f"{ROOT_DIR}/{NEWS_FILE}",sep='\|', engine='python')
    df = df.append({'Stock': stock}, ignore_index=True)
    replace_news_csv(df)

def remove_stock_to_news(stock):
    #load news file from csv
    df = pd.read_csv(f"{ROOT_DIR}/{NEWS_FILE}",sep='\|', engine='python')
    df = df[df.Stock != stock]
    replace_news_csv(df)