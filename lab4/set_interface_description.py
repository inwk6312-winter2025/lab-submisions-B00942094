from netmiko import Netmiko

# Define device connection details
devices = [{
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "port": "22",
}]

# Set the description for the interface
description = 'Description set with Netmiko'
description_config = [
    "interface GigabitEthernet3",
    f"description {description}"
]

# Loop through each device and apply the configuration
for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_config_set(description_config)  # Send configuration commands
    print(output)  # Print the output
    net_connect.disconnect()  # Disconnect from the device

