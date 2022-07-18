import telnetlib
import time
HOST = "192.168.1.1"
#user = input("Enter your remote account: ")
password = 'admin'

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Password:")
#tn.write(user.encode('ascii') + b"\n")
tn.write(password.encode('ascii') + b"\n")
'''if password:
    tn.read_until(b"Password: ")'''
    

tn.read_until(b"ZTE>")
tn.write(b"sys reboot\n")
#tn.write(b"exit\n")
time.sleep(5)
print("done :D")
#print(tn.read_all().decode('ascii'))
