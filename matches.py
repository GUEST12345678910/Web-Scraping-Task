#importing essential libraries

import requests
import json
import pandas as pd
url = "https://eu-offering.kambicdn.org/offering/v2018/888it/listView/football.json"
payload = ""
querystring = {"":["","",""],"lang":"en_GB","market":"GB","client_id":"2","channel_id":"1","ncid":"1656483587042","useCombined":"true"}

#Connecting to the api using GET request

response = requests.request("GET", url, data=payload, params=querystring)
print(response.text)

#loading the data scraped from api and storing it in a list of nested dictionaries
with open ('matches.json',encoding="utf") as f :
    match = json.load(f)
matches = []
for i in match['events']:
    fixtures={'Time of match':i['event']['start'],'Home Team ':i['event']['homeName'],'Away Team':i['event']['awayName'],'Group':i['event']['group']}
    matches.append(fixtures)

#Converting the data to a dataframe to faciltate further analysis

df = pd.DataFrame(matches)
a = match['events'][0]['event']
print(df)
json_string = json.dumps(matches)

#Writing and saving the data into a json file
with open('Match_fixtures.json','w')as l:
    l.write(json_string)
    l.close()
