# We are going to use ConnectHandler, which is a tool in the Netmiko toolbox.
# This tool allows us to establish, use, and manage SSH connections with Python.
from netmiko import ConnectHandler

# We are going to call our tool 'ssh_connection'—you can name it whatever you want.
# Before we use it, we need to 'calibrate' the tool. Calibration means specifying the details it needs to work.
# For ConnectHandler, we specify the type of device we are connecting to, the address, the username, and the password.
ssh_connection = ConnectHandler(
    device_type="cisco_ios",
    host="192.168.1.1",       # Replace with your router's IP address
    username="admin",         # Replace with your username
    password="password"       # Replace with your password
)

# Now that our tool is ready, let's use the 'send_command' function.
# This function sends a command to the device over the SSH connection and retrieves the response.
output = ssh_connection.send_command("show clock")

# Let's see what the device sent back. We'll print the output to the screen.
print(output)

# Finally, we need to clean up. The 'disconnect' function of our tool closes the SSH session.
ssh_connection.disconnect()
