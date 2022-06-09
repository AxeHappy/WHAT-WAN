import requests
import sys
import os.path
import socket
import time

ipFile = "/tmp/ip.log" # Can be modified for Windows by changing this to "C:\temp" or a folder of your choosing
timeout = 10

#Creating Services to gather WAN information using API
class Service:
  url = ""
  def request(self): return requests.get(self.url, timeout=timeout)

class InfoIP(Service):
  name = "InfoIP.io"
  url = "https://api.infoip.io/"
  def ip(self): return self.request().json()["ip"]
    
class Ifconfig(Service):
  name = "IfConfig.me"
  url = "https://ifconfig.me/all.json"
  def ip(self): return self.request().json()["ip_addr"]
   
class IPify(Service):
  name = "IPify.org"
  url = "ttps://api.ipify.org?format=json"
  def ip(self): return self.request().json()["ip"]
    
def request_ip():
  #List Services to try
  services = [InfoIP(), Ifconfig(), IPify()]
  for i in range(len(services)):
        
    services = services[i]
    try:
      start = time.time()
      print("* Requesting current IP with {} ".format(services.name))
      ip = services.ip()
      print("* Request took {} seconds ".format(int(time.time() - start)))
      return ip
    except Exception as error:
      print("* Exception when requesting IP using {} : {} ".format(services, error))
      error = "No avialable services, add more or increase timeout (services = {}, timeout = {})".format(len(services), timeout)
      raise RuntimeError(error)
        
def current_ip():
  return(open(ipFile, "r").readlines()[0])
    
def save_ip(ip):
  f = open(ipFile, "w")
  f.write(str(ip))

if os.path.isfile(ipFile): #Does the file exist already
  request_ip = request_ip()
  current_ip = current_ip()

  if request_ip != current_ip:
    save_ip(ipFile)
    print("* IP has changed from {} to {} ".format(current_ip, request_ip))
    sys.exit(1)
  else:
    print("* IP is still {} ".format(current_ip))
    
else:
  request_ip = request_ip()
  save_ip(request_ip)
  print("* This is the first time you have run this script, a file will be generated in {} to store your current address : {} ".format(ipFile, request_ip))


# Basic Socket - Gets your Hostname and IP    
def ip_scan():
  hostname = socket.gethostname()
  IPAddr = socket.gethostbyname(hostname)
  print('* Hostname : ' + hostname)
  print('* IPv4 : ' + IPAddr)
  
 ip_scan()









