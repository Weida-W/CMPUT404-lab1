import requests

version = requests.__version__

print('Requests version is {v}'.format(v = version))

google_url = requests.get("http:/google.com")

print('google_homepage is {h}'.format(h= google_url))
