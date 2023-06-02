import requests 

URL = "https://www.dnd5eapi.co/api/races"
response = requests.get(URL)

if response.status_code!= 200:
  print("error")

data = response.json()

print(data)

#for key, value in data.items():
  #print (key, value)

#print (data["count"])