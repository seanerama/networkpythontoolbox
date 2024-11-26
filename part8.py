import csv
from netmiko import ConnectHandler
from dotenv import load_dotenv
import os

load_dotenv()

device_type = "cisco_ios"
username = os.getenv("USERNAME")    
password = os.getenv("PASSWORD")    

# Function to read the input CSV file and extract IPs and commands
def read_input_csv(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as input_file:
        reader = csv.reader(input_file)
        # Extract the first row (header) for commands
        header = next(reader)
        # Get commands (excluding the 'IP' column)
        commands = header[1:]
        # Get IP addresses (rows after the header)
        devices = [row[0] for row in reader]
    return devices, commands, header

# Function to write results to an output CSV file
def write_output_csv(file_path, header, rows):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the header (IP + commands)
        writer.writerow(header)
        # Write all the results for each device
        writer.writerows(rows)

# Function to connect to a device and run commands
def connect_and_run_commands(ip, commands):
    # Define the connection parameters for the device
    cisco_router = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': username,
        'password': password,
        'port': 22,
    }
    # Attempt to connect and run commands
    try:
        ssh = ConnectHandler(**cisco_router)
        print(f"Successfully connected to {ip}")
        
        # Run each command and collect the results
        ip_results = [ip]  # Start with the IP in the first column
        for command in commands:
            result = ssh.send_command(command)
            ip_results.append(result.strip())  # Strip extra spaces/newlines
        
        # Disconnect after running commands
        ssh.disconnect()
        return ip_results
    except Exception as e:
        print(f"Failed to connect to {ip}: {str(e)}")
        # Return the error message in place of results for this IP
        return [ip] + [f"Error: {str(e)}"] * len(commands)

# Main function to tie everything together
def main(input_csv, output_csv):
    
    # Step 1: Read the input CSV to get IPs and commands
    devices, commands, header = read_input_csv(input_csv)
    
    # Step 2: Collect results for all devices
    results = []
    for ip in devices:
        result_row = connect_and_run_commands(ip, commands)
        results.append(result_row)
    
    # Step 4: Write the results to an output CSV
    write_output_csv(output_csv, header, results)

# Run the main function if this script is executed directly
if __name__ == "__main__":
    input_csv = 'input_3_devices.csv'  # Input file containing IPs and commands
    output_csv = 'results_part8.csv'  # Output file for results
    main(input_csv, output_csv)