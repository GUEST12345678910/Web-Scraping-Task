import requests
import json
import pandas as pd
url = "https://eu-offering.kambicdn.org/offering/v2018/888it/listView/football.json"

querystring = {"":["","",""],"lang":"en_GB","market":"GB","client_id":"2","channel_id":"1","ncid":"1656483587042","useCombined":"true"}

payload = ""
#response = requests.request("GET", url, data=payload, params=querystring)

#print(response.text)
with open ('matches.json',encoding="utf") as f :
    match = json.load(f)
matches = []
for i in match['events']:
    fixtures={'Time of match':i['event']['start'],'Home Team ':i['event']['homeName'],'Away Team':i['event']['awayName'],'Group':i['event']['group']}
    matches.append(fixtures)

df = pd.DataFrame(matches)
a = match['events'][0]['event']
print(df)
json_string = json.dumps(matches)
with open('Match_fixtures.json','w')as l:
    l.write(json_string)
    l.close()
