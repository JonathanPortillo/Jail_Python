import requests

response = requests.get("https://www.jailbase.com/api/1/recent/?source_id=az-mcso")
print(response.text)
