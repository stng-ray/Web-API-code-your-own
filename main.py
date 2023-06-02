import DND5e

import requests 

URL = "https://www.dnd5eapi.co/api"
response = requests.get(URL)

if response.status_code!= 200:
  print("error")


specify = input("""What would you like randomized? Choices listed below:
ability-scores
alignments
backgrounds
classes
conditions
damage-types
equipment
equipment-categories
feats
features
languages
magic-items
magic-schools
monsters
proficiencies
races
rule-selections
rules
skills
spells
subclasses
subraces
traits
weapon-properties
""")



print(specify)


