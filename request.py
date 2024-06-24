import requests

url = "http://20.244.56.144/test/register"
data = {
    "companyName": "Fullstack",
    "ownerName": "Bobby Nandigam",
    "rollNo": "20kb1a0595",
    "ownerEmail": "bobbynandigam.official@gmai.com",
    "accessCode": "nbYNBp"
}

response = requests.post(url, json=data)

print(response.json())