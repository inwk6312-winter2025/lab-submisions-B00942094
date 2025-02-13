from netmiko import Netmiko
import logging

# Define device connection details
devices = [{
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "port": "22",
}]

# Loop through each device and apply the configuration
for device in devices:
    net_connect = Netmiko(**device)  # Connect to the device
    output = net_connect.send_config_from_file('changes.txt')  # Send configuration commands from file
    print(output)  # Print the output of the configuration
    net_connect.disconnect()  # Disconnect from the device

