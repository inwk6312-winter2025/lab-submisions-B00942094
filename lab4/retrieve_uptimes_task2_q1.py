from netmiko import Netmiko

# List of devices in your topology
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",  # Replace with the actual IP of the router
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",  # Replace with the actual IP of the router
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    },
    # Add more devices here
]

# Loop through each device in the topology
for device in devices:
    try:
        # Establish SSH connection to the device
        net_connect = Netmiko(**device)
        
        # Send the 'show version' command to get device info
        output = net_connect.send_command("show version")
        
        # Disconnect from the device
        net_connect.disconnect()
        
        # Search for 'uptime is' in the output
        result = output.find('uptime is')
        
        if result != -1:
            # Extract the uptime substring
            begin = result
            end = begin + 38  # Length of the 'uptime is' string and following time info
            uptime_info = output[begin:end].strip()
            print(f"{device['ip']} => {uptime_info}")
        else:
            print(f"Uptime information not found for {device['ip']}")

    except Exception as e:
        print(f"Failed to connect to {device['ip']} due to: {e}")

