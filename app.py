import requests
from time import sleep

url_base = 'http://os-sample-python-git:8080'
para = '/api/v1/resources/books/all'
url = url_base + para

n = 0
while True:
    print(n)
    try:
        response = requests.get(url)
        print(response.status_code)
        content = response.json()
        print(content)
    except Exception as E:
        print('something wrong')
        print(E)
    n += 1
    sleep(5)
    if n > 1000:
        break

