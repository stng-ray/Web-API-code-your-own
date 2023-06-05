import requests

URL = "https://www.dnd5eapi.co/api/alignments"
response = requests.get(URL)

if response.status_code != 200:
  print("error")

data = response.json()

#print(data)
count = data['count']
results = data['results']
#print(count)

import random
random_result_ix = random.randint(0, count-1)
random_result = results[random_result_ix]

attribute = input("what attribute would you like? ")

if attribute == "alignment":
  print("here is an alignment:")
  print (random_result["name"])



#for key, value in data.items():
#print (key, value)

#print (data["count"])
