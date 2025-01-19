import requests
import send_email as se
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

API_KEY = os.getenv("APIKEY")
#url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
url = f"https://newsapi.org/v2/everything?q=stocks|bitcoin|crypto&sortBy=publishedAt&pageSize=30&apiKey={API_KEY}"

#pip freeze > requirements.txt, pip install -r requirements.txt

# make request
request = requests.get(url)

# get a dictionary with data
content = request.json()

message_header = 'Subject: Crypto and Stock News\n\n'

message_body = f"""\
From: Auto Mail From App
"""
message_body = message_body + message_header
for article in content["articles"]:
    message_body = message_body + "•****" + str(article["title"]) + "****•" + \
                   "\n" + str(article["description"]) + "\n" + f"Source: {article['url']}" + 2*"\n"

message_body = message_body.encode("utf-8")
se.send_email(message=message_body)