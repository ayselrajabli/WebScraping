import requests as req
import pandas as pd
import re
from bs4 import BeautifulSoup 

url = "https://www.reddit.com/r/gameofthrones/"
response = req.get(url)
soup = BeautifulSoup(response.text, "html.parser")
soup = BeautifulSoup(response.text, "html.parser")

headers_list = list()
headers = soup.findAll("h3", attrs = {"class":"_eYtD2XCVieq6emjKBH3m"})
for header in headers:
    headers_list.append(header.text)
new_headers = list()
for j in headers_list:
    a = re.sub(r"\[.+\] ", r"", j)
    new_headers.append(a)
#print(new_headers)

votes_list = list()
votes = soup.findAll("div", attrs = {"class":"_3a2ZHWaih05DgAOtvu6cIo"})
for vote in votes:
    votes_list.append(vote.text)
#print(votes_list)

dates_list = list()
dates = soup.findAll("a", attrs = {"class":"_3jOxDPIQ0KaOWpzvSQo-1s"})
for date in dates:
    dates_list.append(date.text)
#print(dates_list)

links_list = list()
links = soup.findAll("a", attrs = {"class":"_3jOxDPIQ0KaOWpzvSQo-1s"})
for link in links:
    links_list.append(link.get("href"))
#print(links_list)

df = pd.DataFrame(zip(new_headers, votes_list, dates_list, links_list), columns = ["Headers", "Votes", "Dates", "Links"])
csv_file = df.to_csv("gameofthrones.csv")
reading = pd.read_csv("gameofthrones.csv")
reading.drop(["Unnamed: 0"], axis = 1, inplace = True)

print(reading)
