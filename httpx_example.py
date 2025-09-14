from importlib.metadata import files

import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code)  # 200
print(response.json())       # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}

import httpx

data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)

print(response.status_code)  # 201 (Created)
print(response.json())       # Ответ с созданной записью

headers = {"Authorization": "Bearer my_secret_token"}

response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.status_code)
print(response.json())  # Заголовки включены в ответ

params = {"userId":1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

print(response.status_code)
print(response.json())

files = {"file": ("example.txt", open("example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)

print(response.status_code)
print(response.json())


client = httpx.Client(
    base_url="https://jsonplaceholder.typicode.com" ,
    headers={"Authorization": "Bearer my_secret_token"}
)
response1 = client.get("/todos/1")
response2 = client.get("/todos/2")

print(response1.json())
print(response2.json())


try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")


try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
    print(response.status_code)
except httpx.ReadTimeout as e:
    print("Запрос превысил лимит времени")


