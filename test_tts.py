#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

url = "http://0.0.0.0:2021/tts/"

payload = "{\n\t\"input\" : \"சென்று வருகிறேன்\",\n\t\"language\": \"tamil\"\n}"
headers = {
    'content-type': "application/json",
    'rev-api-key': "036f3b1b68e799b16cc54f0e5c668a4c",
    'rev-app-id': "benchmarking",
    'cache-control': "no-cache",
    'postman-token': "61ed9978-b48c-6d8a-6abd-118771771fe9"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
