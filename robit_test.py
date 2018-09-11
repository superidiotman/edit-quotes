import pytumblr
from config import client, gKey, gsSheetID
import requests
import numpy as np
import time

if False:
  client.create_text("editquotesrobit", body="Third party tiwtter reposetsts? 2.0")
# This should run through IFTTT - sometimes takes a few minutes

sheetRange = "A2:B300"
response = requests.get(f"https://sheets.googleapis.com/v4/spreadsheets/{gsSheetID}/values/Sheet1!{sheetRange}?key={gKey}")
qList = response.json()["values"]

def renderQuote(row):
  return f"{row[0]} -{row[1]}"

np.random.shuffle(qList)

for q in qList:
  print(renderQuote(q))
  time.sleep(10)
# qListLen = len(data["values"])
# print(renderQuote(data["values"][qListLen-1]))