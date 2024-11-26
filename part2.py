from netmiko import ConnectHandler

# We are using the dotenv toolbox to load environment variables.
# Environment variables are a safe place to store sensitive information like usernames, passwords, and IP addresses.
from dotenv import load_dotenv

# We are using the os toolbox to retrieve these environment variables once they are loaded.
# This tool allows us to interact with our computer's operating system, such as accessing files or environment variables.
import os

# Load the environment variables from the .env file
# This helps us keep sensitive information like credentials secure.
load_dotenv()

# Retrieve the credentials and IP address from the .env file
# Think of the .env file as a drawer where we keep all the important details for our tools.
device_type = "cisco_ios"
username = os.getenv("USERNAME9")    # The SSH username
password = os.getenv("PASSWORD9")    # The SSH password
host = '192.168.1.1'

# Now we calibrate our tool using these details.
ssh_connection = ConnectHandler(
    device_type=device_type,
    host=host,
    username=username,
    password=password
)

output = ssh_connection.send_command("show clock")

print(output)

ssh_connection.disconnect()
