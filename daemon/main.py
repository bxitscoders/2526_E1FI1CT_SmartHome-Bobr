import requests

running = True
api_endpoint = "http://localhost/devices/"

while running:
    post(api_endpoint)