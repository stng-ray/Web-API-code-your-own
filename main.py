import requests
url = "https://api.ravelry.com/projects/search.json?query=puppycat"

response = requests.get(url)
ravelry_things = response.json()
ravelry_things

print(ravelry_things)

print("hello Hannah")