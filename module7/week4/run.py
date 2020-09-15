#!/usr/bin/env python3
import os, sys
import json
import requests

path = "supplier-data/descriptions/"
url = "http://localhost/fruits/"

files = os.listdir(path)

for file in files:
  if file.endswith("txt"):
    with open(path + file, 'r') as f:
      #grab the file name, ex. 001, 002 to use for image file
      fruit_name = os.path.splitext(file)[0]
      data = f.read()
      data = data.split("\n")
      fruit_dic = {"name": data[0], "weight": int(data[1].strip(" lbs")), "description": data[2], "image_name": fruit_name + ".jpeg"}
      response = requests.post(url, json=fruit_dic)
      response.raise_for_status()
      print(response.request.url)
      print(response.status_code)