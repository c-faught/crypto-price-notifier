import yagmail
import keyring
from config.secrets import get_config

def send_news_notification(news_tuple):
    stock, time, title, url, category = news_tuple 
    sender_email, recipient_email, password  = get_config("DEV")
    yag = yagmail.SMTP(sender_email, password)
    contents = [f"Posted: {time}",title,url]
    yag.send(recipient_email, f"${stock}: {category} Post", contents)

#news = ("AC:CT","6h ago","Transat caps disastrous year by losing $238.1M in Q4","https", "Company News")
#send_news_notification(news)