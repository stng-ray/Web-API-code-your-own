#import DND5e
#import races
import requests

URL = "https://www.dnd5eapi.co/api/"


def get_info(attribute):
  url = URL + attribute
  response = requests.get(url)
  if response.status_code != 200:
    print("Error calling ", url, ": ", response.status_code)
    return None
  return response.json()


def get_class():
  class_type = input("What class? (s to show all, r for a random class)? ")
  if class_type == "s":
    classes = get_info("classes")
    for the_class in classes["results"]:
      print(the_class["name"])
  elif class_type == "r":
    print("not implemented")
  else:
    the_class = get_info("classes/" + class_type)
    #print (the_class)
    print("hit_die:", the_class["hit_die"])
    print(the_class["proficiencies"])
    for proficiency in the_class["proficiencies"]:
      print("\t", proficiency["name"])


while True:
  get_class()
"""
specify = input("What would you like randomized? Choices listed below")
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
print(specify)
"""
