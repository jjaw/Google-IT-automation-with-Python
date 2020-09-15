In order for cron_file to work, you need to modifiy the health_check.py.
line 34
  receiver = "{}@example.com".format(os.environ["USER"])
to
  receiver = "{user-name}@example.com"

1 * * * * . $HOME/.profile; python3 /home/{user-name}/health_check.py



{user-name} is the username provided by your qwiklabs session
