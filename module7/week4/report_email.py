#!/usr/bin/env python3

import os, datetime
import json
from reports import generate

#get the current time in GMT
current_date = datetime.datetime.now().strftime('%Y-%m-%d')

def generate_pdf(path):
  pdf = ""
  files = os.listdir(path)
  for file in files:
    if file.endswith(".txt"):
      with open(file, 'r') as f:
        inline = f.readlines()
        name = inline[0].strip()
        weight = inline[1].strip()
        pdf += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
  return pdf

if __name__ == "__main__":
  path = "~/supplier-data/descriptions/"
  generate_pdf(path)





