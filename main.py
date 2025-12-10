import sys
import ipaddress
import socket
import os

def SSH(ip):
   try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(3)
      s.connect((ip, 22))
      s.shutdown(2)
      return 1
   except:
      return 0

def bruteforce():
    """
    /// I cannot write this function without crossing legal boundaries.
    /// As a reminder, this script is strictly for educational purposes and has been developed and tested only within a local network.
    /// 
    """

ip4 = ipaddress.IPv4Address("93.113.207.181")
os.system("clear" if os.name != "nt" else "cls")
print("""\n                                __ \n     __ ___    ____ _____  ___ / /_\n    / // / |/|/ / // / _ \/ -_) __/\n    \_,_/|__,__/\_,_/_//_/\__/\__/ \n                                   """)

while True:
   try:
      print(" >>> Analyzing IP Address : "+ str(ip4))
      if(SSH(str(ip4))==1):
         print(" >>> Discover new open SSH port !")
         with open("open_ssh.txt", "w") as f:
             line = f"[SSH] {ip4}"
             f.write(line)
         bruteforce(str(ip4))
      ip4 = ip4+1
   except KeyboardInterrupt:
      sys.exit()
