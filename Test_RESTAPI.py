import requests
URL="http://127.0.0.1:5000/weather"
response=requests.get(URL)
Message = response.json()
print(Message["Country"]+" "+Message["City"]+" "+Message["Temperature"])
print(Message["City"])
print(Message["Temperature"])
