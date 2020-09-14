#! /usr/bin/env python3

import os
import requests

path = "/data/feedback/"
reviews = os.listdir(path)

dict = {}

for review in reviews:
  with open(path + review) as f:
    dict["title"] = f.readline().strip()
    dict["name"] = f.readline().strip()
    dict["date"] = f.readline().strip()
    dict["feedback"] = f.readline().strip()
	
  response = requests.post("http://34.123.16.109/feedback/", json=dict)
  response.raise_for_status()
print(response.status_code)
	
	
