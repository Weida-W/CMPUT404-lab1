import requests

version = requests.__version__

print('Requests version is {v}'.format(v = version))

google_url = requests.get("http://www.google.com")

print(google_url)

myself_url = requests.get("https://raw.githubusercontent.com/Weida-W/CMPUT404-lab1/master/lab1.py")

print(myself_url.text)