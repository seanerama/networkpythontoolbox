from netmiko import ConnectHandler
from dotenv import load_dotenv
import os
#import the csv toolbox
import csv

load_dotenv()

device_type = "cisco_ios"
username = os.getenv("USERNAME9")    
password = os.getenv("PASSWORD9")    

commands = [
    "show clock",
    "show ver | i Last reload reason:"
]

# File paths
ip_file = "ips.txt"  # Text file containing a list of IPs, one per line
output_file = "command_results.csv"  # CSV file to save the command results

#Open the txt file
with open(ip_file, "r") as file:
    # Create an empty list to store the IP addresses
    ips = []

    # Read each line from the file
    for line in file:
        # Remove leading/trailing spaces or newline characters
        stripped_line = line.strip()
        
        # If the line is not empty, add it to the list
        if stripped_line:
            ips.append(stripped_line)

commands = [
    "show clock",
    "show ver | i Last reload reason:"
]

# Open the CSV file for writing
with open(output_file, mode="w", newline="") as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)
    
    # Write the header row
    csv_writer.writerow(["IP Address", "Command", "Output"])

    # Iterate through each IP address
    for ip in ips:

        # Connect to the device
        ssh = ConnectHandler(
            device_type=device_type,
            host=ip,
            username=username,
            password=password
        )

        # Execute each command and write results to the CSV
        for command in commands:
            output = ssh.send_command(command)
            # Write the results as a new row in the CSV
            csv_writer.writerow([ip, command, output])

        # Disconnect from the device
        ssh.disconnect()


# Inform the user where the results were saved
print(f"Results saved to {output_file}")