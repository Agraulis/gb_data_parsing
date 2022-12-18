import requests
import json

url = "https://api.vk.com/method/"
method = "users.getSubscriptions"
params = ""
version = "5.131"
token = "vk1.a.oLvopZbsxjkoJ1aKxE560eLqvmqwjYqOLq7G9IXEPhaDWRktURPtrg4gxjK2UPksU9inug0_2iwIg_WNZnmU5SG-oKZewsgb3MI3M65dth9fq5ojHM3k7vjT25vR5V1papsvf4zi4X3zej1h89gwytCF_G7UJr-4wWKASgGfwldvv6xeYXPn2_MaevK6irCSSBNpEHoJUWUfg8FXfA5zA"
url = f"{url}{method}?{params}&access_token={token}&v={version}"
response = requests.get(url=url)

json_object = json.dumps(response.json(), indent=4)
with open("vk_group_list.json", "w") as outfile:
    outfile.write(json_object)
