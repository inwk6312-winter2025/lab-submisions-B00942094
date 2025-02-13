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
        
        # Search for 'Configuration register is' in the output
        result = output.find('Configuration register is')

        if result != -1:
            # Extract the configuration register value from the output
            config_register = output[result:].splitlines()[0].strip()
            print(f"{device['ip']} => {config_register}")
        else:
            print(f"Configuration register not found for {device['ip']}")

    except Exception as e:
        print(f"Failed to connect to {device['ip']} due to: {e}")

