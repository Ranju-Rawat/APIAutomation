import requests
import json
import jsonpath

# API URL
# url = "https://reqres.in/api/users?page=2"
# resp = requests.get(url)
#
#
# #parse response to json format
#
# json_res = json.loads(resp.content)
# dt = jsonpath.jsonpath(json_res, "total_pages")
# print(dt[0])

url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"
resp = requests.get(url)

json_resp = json.loads(resp.content)

for val in json_resp:
    print(val)
    data = jsonpath.jsonpath(url, val)
    print(data)

#[{'id': 1, 'title': 'Activity 1', 'dueDate': '2024-05-08T05:48:24.134079+00:00', 'completed': False}, {'id': 2, 'title': 'Activity 2', 'dueDate': '2024-05-08T06:48:24.1340818+00:00', 'completed': True}, {'id': 3, 'title': 'Activity 3', 'dueDate': '2024-05-08T07:48:24.1340822+00:00', 'completed': False}, {'id': 4, 'title': 'Activity 4', 'dueDate': '2024-05-08T08:48:24.1340824+00:00', 'completed': True}, {'id': 5, 'title': 'Activity 5', 'dueDate': '2024-05-08T09:48:24.1340827+00:00', 'completed': False}, {'id': 6, 'title': 'Activity 6', 'dueDate': '2024-05-08T10:48:24.1340833+00:00', 'completed': True}, {'id': 7, 'title': 'Activity 7', 'dueDate': '2024-05-08T11:48:24.1340863+00:00', 'completed': False}, {'id': 8, 'title': 'Activity 8', 'dueDate': '2024-05-08T12:48:24.1340867+00:00', 'completed': True}, {'id': 9, 'title': 'Activity 9', 'dueDate': '2024-05-08T13:48:24.1340871+00:00', 'completed': False}, {'id': 10, 'title': 'Activity 10', 'dueDate': '2024-05-08T14:48:24.1340876+00:00', 'completed': True}, {'id': 11, 'title': 'Activity 11', 'dueDate': '2024-05-08T15:48:24.1340879+00:00', 'completed': False}, {'id': 12, 'title': 'Activity 12', 'dueDate': '2024-05-08T16:48:24.1340882+00:00', 'completed': True}, {'id': 13, 'title': 'Activity 13', 'dueDate': '2024-05-08T17:48:24.1340885+00:00', 'completed': False}, {'id': 14, 'title': 'Activity 14', 'dueDate': '2024-05-08T18:48:24.1340888+00:00', 'completed': True}, {'id': 15, 'title': 'Activity 15', 'dueDate': '2024-05-08T19:48:24.1340891+00:00', 'completed': False}, {'id': 16, 'title': 'Activity 16', 'dueDate': '2024-05-08T20:48:24.1340894+00:00', 'completed': True}, {'id': 17, 'title': 'Activity 17', 'dueDate': '2024-05-08T21:48:24.1340897+00:00', 'completed': False}, {'id': 18, 'title': 'Activity 18', 'dueDate': '2024-05-08T22:48:24.1340901+00:00', 'completed': True}, {'id': 19, 'title': 'Activity 19', 'dueDate': '2024-05-08T23:48:24.1340904+00:00', 'completed': False}, {'id': 20, 'title': 'Activity 20', 'dueDate': '2024-05-09T00:48:24.1340906+00:00', 'completed': True}, {'id': 21, 'title': 'Activity 21', 'dueDate': '2024-05-09T01:48:24.1340909+00:00', 'completed': False}, {'id': 22, 'title': 'Activity 22', 'dueDate': '2024-05-09T02:48:24.1340912+00:00', 'completed': True}, {'id': 23, 'title': 'Activity 23', 'dueDate': '2024-05-09T03:48:24.1340915+00:00', 'completed': False}, {'id': 24, 'title': 'Activity 24', 'dueDate': '2024-05-09T04:48:24.1340918+00:00', 'completed': True}, {'id': 25, 'title': 'Activity 25', 'dueDate': '2024-05-09T05:48:24.1340921+00:00', 'completed': False}, {'id': 26, 'title': 'Activity 26', 'dueDate': '2024-05-09T06:48:24.1340924+00:00', 'completed': True}, {'id': 27, 'title': 'Activity 27', 'dueDate': '2024-05-09T07:48:24.1340927+00:00', 'completed': False}, {'id': 28, 'title': 'Activity 28', 'dueDate': '2024-05-09T08:48:24.134093+00:00', 'completed': True}, {'id': 29, 'title': 'Activity 29', 'dueDate': '2024-05-09T09:48:24.1340932+00:00', 'completed': False}, {'id': 30, 'title': 'Activity 30', 'dueDate': '2024-05-09T10:48:24.1340935+00:00', 'completed': True}]
