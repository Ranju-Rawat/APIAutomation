import json

import jsonpath
import requests


url = "https://reqres.in/api/users/2"
file = open("C:\\Users\\rawat\\OneDrive\\Desktop\\create_user.txt", "r")
json_input = file.read()
req_json = json.loads(json_input)

#make put method

response = requests.put(url, req_json)
resp_json = json.loads(response.text)
update_data = jsonpath.jsonpath(resp_json, "updatedAt")
print(resp_json)