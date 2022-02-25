import requests
data = {"userId": 5,
    "id": 47,
    "title": "quibusdam cumque rem aut deserunt",
    "body": "voluptatem assumenda ut voluptate"}
#response = requests.get("https://jsonplaceholder.typicode.com/")
response = requests.post(url = "https://jsonplaceholder.typicode.com/posts", data = data)
print(response.status_code)
#print(response)