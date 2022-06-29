import requests
import json
import pandas as pd 

url = "https://sportclient-uc.safe-iplay.com/sports"

querystring = {"lang":"en_GB","market":"GB","offering":"888it","useProdApis":"false"}
#uniqueKeyToGroupDetails
#sportGroups
payload = ""
#response = requests.request("GET", url, data=payload, params=querystring)
with open ('league.json','r') as f :
    ang = json.load(f)
football=[]
basketball=[]
baseball=[]
tennis=[]
volleyball=[]
for i in ang['uniqueKeyToGroupDetails'].keys():
    if i.startswith('football'):
        football.append(i.split('-')[-1])
    elif i.startswith('basketball'):
        basketball.append(i.split('-')[-1])
    elif i.startswith('baseball'):
        baseball.append(i)
    elif i.startswith('tennis'):
        tennis.append(i.split('-')[-1])
    elif i.startswith('volleyball'):
        volleyball.append(i.split('-')[-1])
        
def save_data(sport_league):
    json_string = json.dumps(volleyball)
    with open('tennis_leagues.json','w') as t:
        t.write(json_string)
        t.close()
        
   
