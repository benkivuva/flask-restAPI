import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"likes": 12, "name": "mwawasi", "views": 21900},
    {"likes": 8, "name": "funny_cats", "views": 55000},
    {"likes": 15, "name": "epic_adventures", "views": 123456},
    {"likes": 10, "name": "cooking_masterclass", "views": 9800},
    {"likes": 20, "name": "travel_diaries", "views": 75000}
]

# Function to send a DELETE request for a video
def delete_video(video_id):
    response = requests.delete(BASE + "video/" + str(video_id))
    print("DELETE Response for video", video_id, ":", response.text)

# Function to send a PATCH request to update a video
def update_video(video_id, updated_data):
    response = requests.patch(BASE + "video/" + str(video_id), json=updated_data)
    print("PATCH Response for video", video_id, ":", response.json())

# Iterate through the data and send POST requests to create videos
for i, video in enumerate(data):
    response = requests.post(BASE + "video/" + str(i), json=video)
    print("POST Response for video", i, ":", response.json())

# Wait for user input
input("Press Enter to continue...")

# Send GET requests to retrieve the created videos
for i in range(len(data)):
    response = requests.get(BASE + "video/" + str(i))
    print("GET Response for video", i, ":", response.json())

# Update the first video
updated_data = {"likes": 30, "views": 100000}
update_video(0, updated_data)

# Wait for user input
input("Press Enter to continue...")

# Delete the second video
delete_video(1)

# Wait for user input
input("Press Enter to continue...")

# Try to get the deleted video (should return a 404 status code)
response = requests.get(BASE + "video/1")
print("GET Response for deleted video:", response.status_code)

