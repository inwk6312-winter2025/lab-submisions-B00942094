from netmiko import ConnectHandler

# List of routers in your topology
routers = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",  # Replace with the actual IP of router 1
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",  # Replace with the actual IP of router 2
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    },
    # Add more routers here
]

# Loop through each router in the topology
for device in routers:
    try:
        # Establish SSH connection to the device
        net_connect = ConnectHandler(**device)
        
        # Send the 'show interface description' command to get interface details
        output = net_connect.send_command("show interface description")
        
        # Disconnect from the device
        net_connect.disconnect()
        
        # Print output for this device
        print("-" * 100)
        print(f"Interfaces for device: {device['ip']}")
        print(output)
        print("-" * 100)
    
    except Exception as e:
        print(f"Failed to connect to {device['ip']} due to: {e}")

