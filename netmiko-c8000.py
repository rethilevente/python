from netmiko import ConnectHandler
from getpass import getpass

cisco1 = { 
    "device_type": "cisco_ios",
    "host":"172.19.255.216",
    "username": "admin",
    "password": getpass(),
}

command = "show ip int brief"

with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)
print(output)
