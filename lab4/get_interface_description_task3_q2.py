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

# List of show commands to run on each router
commands = [
    "show version",
    "show interface description",
    "show ip interface brief",
    "show running-config",
    "show ip route",
    "show vlan brief",
    "show startup-config"
    # Add more show commands as needed
]

# Loop through each router in the topology
for device in routers:
    try:
        # Establish SSH connection to the device
        net_connect = ConnectHandler(**device)
        
        # Loop through each show command and execute it
        for command in commands:
            print("-" * 100)
            print(f"Output for {device['ip']} - {command}:")
            output = net_connect.send_command(command)
            print(output)
            print("-" * 100)
        
        # Disconnect from the device
        net_connect.disconnect()
    
    except Exception as e:
        print(f"Failed to connect to {device['ip']} due to: {e}")

