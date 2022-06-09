import requests
import sys
import os.path
import socket
#import smtplib
import time

ipFile = "/tmp/ip.log"
#html_doc = requests.get("https://api.infoip.io/")
timeout = 10

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
  #List Services
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

if os.path.isfile(ipFile): #Does it exist
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
    


"""
if os.path.isfile(ipFile) : #File exists
  request_ip = request_ip()  
  current_ip = current_ip()

  if request_ip != current_ip:
    save_ip(request_ip)
    print ("* IP has changed from {} to {}".format(current_ip, request_ip))
    sys.exit(1)
  else:
    print ("* IP is still the same: {}".format(current_ip))
else:
  request_ip = request_ip()
  save_ip(request_ip)
  print ("* This is the first time to run the ip_change script, I will create a file in {} to store your current address: {} ".format(ipFile, request_ip))
"""

# def ip_request():
    # wan = html_doc.text[6:22]
    # text = wan.strip(' " ')
    # code = html_doc.status_code
    # print("Your WAN IP : " + text)
    # print("Status Code : " + str(code))
    
def ip_scan():
  hostname = socket.gethostname()
  IPAddr = socket.gethostbyname(hostname)
  print('* Hostname : ' + hostname)
  print('* IPv4 : ' + IPAddr)
        
ip_scan()



#NOTES
#print(html_doc.status_code) #Check Status Code of request (ie, 404, 200)
#print(html_doc.headers) #returns a python dict containing key-value pairs of the headers

#print(html_doc.encoding)
#html_doc.encoding = 'utf-8'
#Requests library also allows you to see or
#change the encoding of the response content.







