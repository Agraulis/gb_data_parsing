import json
import requests

url = "https://api.github.com/users/Agraulis/repos"
response = requests.get(url=url)
json_object = json.dumps(response.json(), indent=4)
with open("repos_list.json", "w") as outfile:
    outfile.write(json_object)
