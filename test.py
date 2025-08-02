import requests

response = requests.get('https://api.github.com/emojis')
print(response.json())

