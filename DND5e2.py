import requests

URL = "https://www.dnd5eapi.co/api/"

attribute = input("what attribute would you like? ").lower().strip()
allowed_attributes = ["ability-scores", "alignments", "backgrounds", "classes", "conditions", "damage-types", "equipment", "equipment-categories", "feats", "features", "languages", "magic-items", "magic-schools", "monsters", "proficiencies", "races", "rule-selections", "rules", "skills", "spells", "subclasses", "subraces", "traits", "weapon-properties"]
while attribute not in allowed_attributes:
  attribute = input("Choose one of", allowed_attributes, ": ")

NewURL = URL + attribute

response = requests.get(NewURL)

if response.status_code != 200:
  print("error")

data = response.json()


#print(data)
count = data['count']
results = data['results']
#print(count)

import random

random_result_ix = random.randint(0, count - 1)
random_result = results[random_result_ix]

print(random_result["name"])

#for key, value in data.items():
#print (key, value)

#print (data["count"])
