from netmiko import Netmiko

# Device connection details
device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",  # Change this IP as needed
    "username": "student",
    "password": "Meilab123",
    "port": "22"
}

# Establish SSH connection
net_connect = Netmiko(**device)

# Get the output of the 'show ip interface brief' command using TextFSM parsing
output = net_connect.send_command("show ip interface brief", use_textfsm=True)

# Disconnect from the device
net_connect.disconnect()

# Print the type of the output (it should now be a list)
print(type(output))

# Loop through the parsed output and print each interface's name (intf)
for interface in output:
    print(interface['intf'])

