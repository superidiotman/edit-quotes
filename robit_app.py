web=True

import pytumblr
import requests
import numpy as np
import time
import os

if web:
  client = pytumblr.TumblrRestClient({os.environ.get('consumer_key'),
      os.environ.get('consumer_secret'), os.environ.get('access_token'),
      os.environ.get('access_secret')})
  gKey = os.environ.get('gKey')
  gsSheetID = os.environ.get('gsSheetID')
else:
  from config import client, gKey, gsSheetID

sheetRange = "A2:B300"
response = requests.get(f"https://sheets.googleapis.com/v4/spreadsheets/{gsSheetID}/values/Sheet1!{sheetRange}?key={gKey}")
qList = response.json()["values"]

def renderQuote(row):
  return f"{row[0]} -{row[1]}"

np.random.shuffle(qList)

for q in qList:
  client.create_text("editquotesrobit", body=renderQuote(q))
  # Posts to Tumblr, which x-posts to Twitter through IFTTT - sometimes takes a few minutes
  print("tweeted another")
  time.sleep(2500)