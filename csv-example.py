import csv

# Open the CSV file in read mode
with open('data.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Read the header row first (if there is one)
    header = next(csv_reader)
    print("Header:", header)
    
    # Loop through each row in the CSV file
    print("Data:")
    for row in csv_reader:
        print(row)

devices = [
    {"Device Name": "Router1", "IP Address": "192.168.1.1", "Status": "Up"},
    {"Device Name": "Switch1", "IP Address": "192.168.1.2", "Status": "Down"},
    {"Device Name": "Firewall1", "IP Address": "192.168.1.3", "Status": "Up"},
    {"Device Name": "AP1", "IP Address": "192.168.1.4", "Status": "Down"},
]

filename = 'devices.csv'

# Open the CSV file in write mode
with open(filename, mode='w', newline='') as file:
    # Create a CSV DictWriter object, using the keys from the first dictionary as the header
    fieldnames = devices[0].keys()
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Write the header (field names) to the CSV
    csv_writer.writeheader()
    
    # Write each dictionary as a row in the CSV
    for device in devices:
        csv_writer.writerow(device)

print(f"Data has been written to {filename}")