from netmiko import ConnectHandler
from dotenv import load_dotenv
import os

load_dotenv()

device_type = "cisco_ios"
username = os.getenv("USERNAME9")    
password = os.getenv("PASSWORD9")    

#now a list of devices
hosts = ['192.168.1.1', '192.168.10.1', '192.168.20.1']              

commands = [
    "show clock",
    "show ver | i Last reload reason:"
]


# Outer loop: Iterates through each host in the 'hosts' list
for host in hosts:
     # Connect to the current host in the loop
    ssh = ConnectHandler(
        device_type=device_type,
        host=host,  # Use the current host from the list
        username=username,
        password=password
    )

    results = "" # Clear results for each device

    # Inner loop: Iterates through each command for the current device
    for command in commands:
        output = ssh.send_command(command)
        results += f"Command: {command}\n{output}\n\n"

    # Print results for the current device
    # The 'f' before the quotes makes this an f-string, allowing us to insert variables directly into the string.
    # `{host}` dynamically inserts the value of the current device's IP into the output.
    # `{results}` inserts the collected command outputs for that device.
    print(f"Results for device {host}:\n{results}")

ssh.disconnect()
