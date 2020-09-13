#!/usr/bin/env python3

import reqesusts

url = "http://localhost/upload/"
path = "~/supplier-data/images/"

images = os.listdir(path)

for image in images:
  if image.endswith(".jpeg"):
    with open(image, 'rb') as opened:
      r = reqeusts.post(url, files={'file': opened})
