import requests
h = {"x-api-key": "DEMO_API_KEY"}
try:
        reply=requests.get("https://api.thecatapi.com/V1/breeds")
except:
        print("Hiba!!")
        exit()
if reply.status_code == 200:
        print(reply.json())
print(reply.status_code)

