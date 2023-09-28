import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"likes": 12, "name": "mwawasi", "views": 21900},
    {"likes": 8, "name": "funny_cats", "views": 55000},
    {"likes": 15, "name": "epic_adventures", "views": 123456},
    {"likes": 10, "name": "cooking_masterclass", "views": 9800},
    {"likes": 20, "name": "travel_diaries", "views": 75000}]

for i in range(len(data)):
    response = requests.post(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + "video/2")
print(response.json())
