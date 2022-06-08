import requests
from bs4 import BeautifulSoup
import csv
import re

url = "https://ja.wikipedia.org"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
top_entry = soup.find("div", attrs={"id": "on_this_day"})
entries = top_entry.find_all("li")
today_list = []

for i, entry in enumerate(entries):
    today_list.append([i + 1, entry.get_text()])
    today_text = entry.get_text().replace("（","(").replace("）",")")

with open("output.csv", "w", encoding="Shift_JIS") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerows(today_list)