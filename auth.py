import requests

# Define the URL for authentication
url = "http://20.244.56.144/test/auth"

# Define the authentication data
data = {
    "companyName": "Fullstack",
    "clientID": "63c1bbd6-f9f9-4c72-a573-1be19ebe830b",
    "clientSecret": "KcPmaktdUzpPmNcy",
    "ownerName": "Bobby Nandigam",
    "ownerEmail": "bobbynandigam.official@gmai.com",
    "rollNo": "20kb1a0595"
}

# Send the POST request
response = requests.post(url, json=data)

# Check the response and print it as JSON
try:
    response_data = response.json()
    print("Response:", response_data)
except ValueError:
    print("Failed to parse response as JSON.")
    print("Response Text:", response.text)
