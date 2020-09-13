#!/usr/bin/env python3

fromPIL import Image
import os, sys

path = "~/supplier-data/images/
pictures = os.listdir(path)

for pic in images:
  outfile = "~/supplier-data/images/" + image
  try:
    Image.open(pic).resize((600,400)).convert("RGB").save(outfile,"JPEG")
  except IOError:
    print("cannot convert", pic)

