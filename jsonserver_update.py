import requests

car = {
      "id": "9",
      "brand": "Skoda",
      "model": "Octavia",
      "production_year": 2025,
      "convertible": False
    }
try:
        reply=requests.post("http://localhost:3000/cars/", json = car)
except:
        print("Hiba!!")
        exit()
print(reply.status_code)
