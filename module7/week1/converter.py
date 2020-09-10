#!/usr/bin/env python3

import os, sys
from PIL import Image

for root, dirs, files in os.walk("."):
  for file in files:
    f, e = os.path.splitext(file)
    outfile = "/opt/icons/" + f
    try:
      #print(outfile)
      Image.open(file).rotate(270).resize((128,128)).convert("RGB").save(outfile, "JPEG")

    except IOError:
      print("cannot convert", file)


