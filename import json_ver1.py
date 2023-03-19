import json
import telnetlib

# read the JSON configuration file
with open('importv1.json', 'r') as f:
    data = json.load(f)

# extract the configuration parameters
host = data['autoap']['host']
username = data['autoap']['username']
password = data['autoap']['password']
enpass = data['autoap']['enpass']
hostname = data['autoap']['hostname']
ssid = data['autoap']['ssid']
authen = data['autoap']['authen']
keyman = data['autoap']['keyman']
wifipass = data['autoap']['wifipass']
channl = data['autoap']['channl']
encmod = data['autoap']['encmod']

# connect to the autoap using telnetlib
tn = telnetlib.Telnet(host)
tn.read_until(b"Username: ")
tn.write(username.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")
tn.write(b"enable\n")
tn.read_until(b"Password: ")
tn.write(enpass.encode('ascii') + b"\n")

# enter configuration mode and configure the interface
tn.write(b"conf t\n")
tn.write(b"hostname " + hostname.encode('ascii') + b"\n")
tn.write(b"Dot11 ssid " + ssid.encode('ascii') + b"\n")
tn.write(b"authentication " + authen.encode('ascii') + b"\n")
tn.write(b"authentication key-management " + keyman.encode('ascii') + b"\n")
tn.write(b"wpa-psk ascii " + wifipass.encode('ascii') + b"\n")
tn.write(b"guest-mode " + b"\n")
#
tn.write(b"Default Int Dot11Radio 0" + b"\n")
tn.write(b"Int Dot11Radio 0" + b"\n")
tn.write(b"Channel " + channl.encode('ascii') + b"\n")
tn.write(b"no shut\n")
tn.write(b"encryption mode ciphers " + encmod.encode('ascii') + b"\n")
tn.write(b"ssid " + ssid.encode('ascii') + b"\n")
#
# exit configuration mode and exit telnet session
tn.write(b"end\n")
tn.write(b"exit\n")
#print(tn.read_all().decode('ascii'))
print(tn.read_all().decode('ascii'))
tn.close()
