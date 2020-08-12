#!/usr/bin/env python3

import re
import csv
import operator

error_msg = {}
user_count = {}

pattern = r"ticky: ([\w]{4,5}) ([\w\s]+)[\[\]#\d\s]*\((\w*)"

logfile = "syslog.log"

err_file = "error_message.csv"
usr_stat = "user_statistics.csv"


with open(logfile) as f:
  for log in f:
    if re.search(pattern, log):
      result = re.search(pattern, log)
      type = result.group(1) #log type
      emsg = result.group(2).strip() #error message
      user = result.group(3) #user name

      if type == "ERROR":
        if emsg not in error_msg.keys():
          error_msg[emsg] = 0
        error_msg[emsg] += 1

      if user not in user_count.keys():
        user_count[user] = {}
        user_count[user]["INFO"] = 0
        user_count[user]["ERROR"] = 0

      if type == "ERROR":
        user_count[user]["ERROR"] += 1
      elif type == "INFO":
        user_count[user]["INFO"] += 1

error_msg = sorted(error_msg.items(), key = operator.itemgetter(1), reverse=True)
user_count = sorted(user_count.items())

f.close()

with open(err_file, 'w') as f:
  writer = csv.writer(f)
  writer.writerow(["ERROR", "COUNT"])
  writer.writerows(error_msg)
f.close()

with open(usr_stat, 'w') as f:
  writer = csv.writer(f)
  writer.writerow(["USERNAME", "INFO", "ERROR"])
  for line in user_count:
    writer.writerow([line[0], line[1]["INFO"], line[1]["ERROR"]])
f.close()


