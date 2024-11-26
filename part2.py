# We are going to use the ConnectHandler tool from the Netmiko toolbox.
# It allows us to establish, use, and manage SSH connections with Python.
from netmiko import ConnectHandler
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
# This helps us keep sensitive information like credentials and IP addresses secure.
load_dotenv()

# Retrieve the credentials and IP address from the .env file
# Think of the .env file as a drawer where we keep all the important details for our tools.
device_type = "cisco_ios"
host = os.getenv("DEVICE_IP")       # The IP address of the router
username = os.getenv("USERNAME")    # The SSH username
password = os.getenv("PASSWORD")    # The SSH password

# Now we calibrate our tool using these details.
ssh_connection = ConnectHandler(
    device_type=device_type,
    host=host,
    username=username,
    password=password
)

# Use the 'send_command' function to send the 'show clock' command to the device.
# This function asks the device for information and brings the response back.
output = ssh_connection.send_command("show clock")

# Print the output to the screen so we can see what the device sent back.
print(output)

# Clean up by closing the SSH session with the 'disconnect' function of our tool.
ssh_connection.disconnect()
