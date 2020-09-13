#!/usr/bin/env python3

from PIL import Image
import os, sys

path = "~/supplier-data/images/
pictures = os.listdir(path)

for pic in images:
  outfile = "~/supplier-data/images/" + image + ".jpeg"
  try:
    Image.open(pic).resize((600,400)).convert("RGB").save(outfile,"JPEG")
  except IOError:
    print("cannot convert", pic)

