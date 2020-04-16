import requests
from time import sleep

url_base = 'http://127.0.0.1:5000'
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
    except:
        print('something wrong')
    n += 1
    sleep(5)
    if n > 1000:
        break

