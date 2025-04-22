import requests

payload = {"text": "Hello, Microservice World!"}
response = requests.post("http://localhost:5000/length", json=payload)

print("Response from microservice:", response.json())
