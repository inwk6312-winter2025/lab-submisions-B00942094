import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import Netmiko

# Load YAML files containing host and interface information
hosts = yaml.load(open('hosts.yml'), Loader=yaml.SafeLoader)
interfaces = yaml.load(open('interfaces.yml'), Loader=yaml.SafeLoader)

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('.'), trim_blocks=True, autoescape=True)

# Load the template for interface configuration
template = env.get_template('interfaces_config_template.j2')

# Render the loopback configuration from the template and interface data
loopback_config = template.render(data=interfaces)

# Loop through all hosts in the YAML file
for host in hosts["hosts"]:
    # Establish connection to the device
    net_connect = Netmiko(
        host=host["name"],
        username=host["username"],
        password=host["password"],
        port=host["port"],
        device_type=host["type"]
    )
    print(f"Logged into {host['name']} successfully")
    
    # Send the configuration set to the device
    output = net_connect.send_config_set(loopback_config.split("\n"))
    prin

