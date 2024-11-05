import requests

url = 'https://jsonplaceholder.typicode.com/posts'

title = input("Введите название: ")
body = input("Введите тело: ")
user_id = input("Введите user_id: ")
response = requests.post(url, data={
    'title': title,
    'body': body,
    'userId': user_id,
})

if response.status_code == 201:
    data = response.json()
    print(data['id'])
elif(response.status_code == 404):
    print(f'Ошибка 404: {response.text}')
elif(response.status_code == 400):
    print(f'Ошибка 400: {response.text}')
else:
    print(f"Ошибка {response.status_code}")   