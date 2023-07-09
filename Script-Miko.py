import requests
import netmiko
import json
from netmiko import ConnectHandler

cisco1 = { 
    "ip": "192.168.10.7",
    "device_type": "cisco_ios",
    "username": "cisco",
    "password": "cisco123!",
}

# Mostrar la información de las IP y estado de las interfaces.
command = "show ip interface brief"


with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)


# Automatically cleans-up the output so that only the show output is returned

print()
print(output)
print()


# Mostrar el running-config.
command = "show run"


with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)


# Automatically cleans-up the output so that only the show output is returned

print()
print(output)
print()


# Mostrar la version .
command = "show version"


with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)


# Automatically cleans-up the output so that only the show output is returned

print()
print(output)
print()