from netmiko import Netmiko

# Define device connection details
devices = [{
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "port": "22",
}]

# Set the description and IP address for the Loopback interface
description = 'Loopback interface created with Netmiko'
loopback_ip = '192.168.100.1 255.255.255.255'

# Configuration commands for the Loopback interface
loopback_config = [
    "interface Loopback0",  # Create Loopback interface
    f"ip address {loopback_ip}",  # Assign IP address
    f"description {description}"  # Set description
]

# Loop through each device and apply the configuration
for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_config_set(loopback_config)  # Send configuration commands
    print(output)  # Print the output of the configuration commands
    net_connect.disconnect()  # Disconnect from the device

