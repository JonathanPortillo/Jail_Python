import requests
import json

response = requests.get("https://www.jailbase.com/api/1/recent/?source_id=az-mcso")
response_dic =json.loads(response.text)
records = (response_dic['records'])
print(records[1]['name'])
