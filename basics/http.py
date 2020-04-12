import requests

def get():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print("get => ", response)

def post():
    url = 'https://jsonplaceholder.typicode.com/posts'
    headers = {
        "Content-type": "application/json; charset=UTF-8",
        "Authorization": "test"
    }
    payload = {
        title: 'foo',
        body: 'bar',
        userId: 1
    }
    response = requests.post(url, data = payload, headers = headers)
    print("post => ", response)

def put():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    headers = {
        "Content-type": "application/json; charset=UTF-8",
        "Authorization": "test"
    }
    payload = {
        id: 1,
        title: 'foo',
        body: 'bar',
        userId: 1
    }
    response = requests.put(url, data = payload, headers = headers)
    print("put => ", response)

def delete():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    response = requests.delete(url, headers = headers)
    print("delete => ", response)


get()
put()
posy()
delete()