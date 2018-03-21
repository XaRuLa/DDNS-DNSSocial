import requests
import time
from urllib2 import urlopen

def timee():
	timenow = time.ctime()
	return timenow


oldip = ""
while True:
 try:
  myip = urlopen('http://ip.42.pl/raw').read()
  if myip == oldip:
   print timee()
   print " "
   time.sleep(59)
  else:
   data = [('host', 'noname.in-malaysia.com'),('auth_token', 'Kaesr1zKctNfbZ5ERSia'),('ip', myip),]
   get_resp = requests.post('https://manage.dnssocial.com/myapi/v1/ddns', data=data)
   oldip = myip
   print timee()
   print get_resp
   print " "
   time.sleep(59)
 except:
  print "No Connections"
  time.sleep(10)
  print " "
