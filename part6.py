import csv
from netmiko import ConnectHandler
from dotenv import load_dotenv
import os

load_dotenv()

device_type = "cisco_ios"
username = os.getenv("USERNAME9")    
password = os.getenv("PASSWORD9")    

# Open the input CSV file that contains the IP addresses and commands
with open('input_3_devices.csv', 'r', encoding='utf-8-sig') as input_file:
    reader = csv.reader(input_file)

    # Extract the first row as the header (contains IP and command columns)
    header = next(reader)

    # Extract the commands (everything after 'IP' in the header)
    commands = header[1:]  # Exclude the 'IP' column

    # Open the results CSV file for writing (output file)
    with open('results_part6.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header back to the results file (same as the input header)
        writer.writerow(header)

        # Loop through each row in the input CSV (each device)
        for row in reader:
            ip = row[0]  # First column is the IP address

            # Define the connection parameters for the device
            cisco_router = {
                'device_type': 'cisco_ios',
                'host': ip,
                'username': username,
                'password': password,
                'port': 22,
            }


            ssh = ConnectHandler(**cisco_router)
            print(f"Successfully connected to {ip}")
            
            # Initialize the row for this device with the IP address as the first element
            ip_results = [ip]
            
            # Run each command and append the result to the row
            for command in commands:
                result = ssh.send_command(command)
                ip_results.append(result.strip())  # Strip any extra whitespace/newlines
            
            # Write the results to the CSV file
            writer.writerow(ip_results)
            
            # Disconnect from the device
            ssh.disconnect()


