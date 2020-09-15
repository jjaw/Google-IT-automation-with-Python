#!/usr/bin/env python3

import psutil, shutil
import socket
import emails
import os, sys

#Warning if CPU usage is over 80%
def cpu_check():
  cpu_usage = psutil.cpu_percent(1) 
  return not cpu_usage > 80

#Report an error if available disk space is lower than 20%
def disc_space_check():  
  disk_usage = shutil.disk_usage("/")
  disk_total = disk_usage.total
  disk_free = disk_usage.used
  threshold = disk_free / disk_total * 100
  return threshold > 20

#Report an error if available memory is less than 500MB
def available_memory_check():
  available = psutil.virtual_memory().available
  available_in_MB = available / 1024 ** 2 #convert to MB
  return available_in_MB > 500

#Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
def hostname_check():
  local_host_ip = socket.gethostbyname('localhost')
  return local_host_ip == "127.0.0.1"

def email_warning(error):
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ["USER"])
  subject = error
  body = "Please check your system and resolve the issue as soon as possible."
  message = emails.generate_email(sender, receiver, subject, body)
  emails.send_email(message)

if not cpu_check():
  subject = "Error - CPU usage is over 80%"
  email_warning(subject)

if not disc_space_check():
  subject = "Error - Available disk space is less than 20%"
  email_warning(subject)

if not available_memory_check():
  subject = "Error - Available memory is less than 500MB"
  email_warning(subject)

if not hostname_check():
  subject = "Error - localhost cannot be resolved to 127.0.0.1"
  email_warning(subject)
