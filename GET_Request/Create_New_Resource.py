import json
import requests
import jsonpath

url = "https://randomuser.me/"

#Read input json file

# file = open("C:\\Users\\rawat\\OneDrive\\Desktop\\create_user.txt", "r")
# json_input = file.read()
# req_json = json.loads(json_input)
#
# #make post request with json body
#
# resp_obj = requests.post(url, json_input)
#
# #parse response into json format
#
# json_format = json.loads(resp_obj.content)
#
# #pick id using json path
#
# data = jsonpath.jsonpath(json_format, "id")
# print(data[0])

file = open("C:\\Users\\rawat\\OneDrive\\Desktop\\create_user1.txt", "r")
file_input = file.read()
req_json = json.loads(file_input)
response_api = requests.post(url, req_json)
print(response_api.content)


