from netmiko import ConnectHandler
from dotenv import load_dotenv
import os

load_dotenv()


device_type = "cisco_ios"
username = os.getenv("USERNAME")    
password = os.getenv("PASSWORD")    
host = '192.168.1.1'                

# A list of commands we want to send to the device
commands = [
    "show clock",
    "show ver | i Last reload reason:"
]

ssh = ConnectHandler(
    device_type=device_type,
    host=host,
    username=username,
    password=password
)

# Let's prepare a variable to store the results of all commands.
results = ""

# Using a 'for loop' to send multiple commands
# The 'for loop' cycles through each item in the 'commands' list, one at a time.
for command in commands:
    # Send the current command to the device and get the output.
    output = ssh.send_command(command)
    # Append the output to the 'results' variable, adding a newline for readability.
    results += f"Command: {command}\n{output}\n\n"

# Print the combined results of all commands.
print(results)

ssh.disconnect()
