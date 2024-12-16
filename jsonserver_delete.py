import requests
id=input("Melyik kocsit szeretned torolni? ")
try:
        reply=requests.delete("http://localhost:3000/cars/" +id)
except:
        print("Hiba!!")
        exit()
print(reply.status_code)
