

---

# **Python Network Toolbox: A Learning Journey**

This repository is a step-by-step guide for network engineers to learn Python by building scripts that interact with network devices. Each part introduces new programming concepts and tools, gradually building a powerful and efficient network automation tool.

---

## **Table of Contents**

1. [Setup Instructions](#setup-instructions)
2. [Scripts Overview](#scripts-overview)
   - [Part 1: Introduction to Netmiko](#part-1-introduction-to-netmiko)
   - [Part 2: Using `dotenv` and `os` Libraries](#part-2-using-dotenv-and-os-libraries)
   - [Part 3: Sending Multiple Commands with a For Loop](#part-3-sending-multiple-commands-with-a-for-loop)
   - [Part 4: Nested For Loops for Multiple Devices](#part-4-nested-for-loops-for-multiple-devices)
   - [Part 5: Reading from Text and Writing to CSV](#part-5-reading-from-text-and-writing-to-csv)
   - [Part 6: Input and Output via CSV Files](#part-6-input-and-output-via-csv-files)
   - [Part 7: Error Handling with Try-Except-Finally](#part-7-error-handling-with-try-except-finally)
   - [Part 8: Refactoring with Functions](#part-8-refactoring-with-functions)
   - [Part 9: Efficiency with `concurrent.futures`](#part-9-efficiency-with-concurrentfutures)

---

## **Setup Instructions**

Follow these steps to set up your environment:

### 1. **Install Python**
Ensure Python 3.8 or higher is installed on your system. Download it [here](https://www.python.org/downloads/).

### 2. **Clone the Repository**
Clone this repository to your local machine:
```bash
git clone https://github.com/seanerama/networkpythontoolbox.git
cd networkpythontoolbox
```

### 3. **Set Up a Virtual Environment**
Create and activate a virtual environment to keep dependencies isolated:
```bash
python3 -m venv network-toolbox-env
source network-toolbox-env/bin/activate  # For Linux/macOS
network-toolbox-env\Scripts\activate     # For Windows
```

### 4. **Install Dependencies**
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### 5. **Prepare a `.env` File**
Create a `.env` file in the root directory to securely store credentials:
```
USERNAME=your_username
PASSWORD=your_password
```

### 6. **Prepare Input Files**
- Create `ips.txt` or `input_devices.csv` files as needed by each script.

---

## **Scripts Overview**

### **Part 1: Introduction to Netmiko**
- **Concepts**: Importing libraries, using the Netmiko toolbox.
- **Purpose**: Connect to a Cisco router and run the `show clock` command.
- **Learning Points**:
  - How to import Python libraries.
  - What Netmiko is and how it helps manage SSH connections.
- **Run**:
  ```bash
  python part1.py
  ```

---

### **Part 2: Using `dotenv` and `os` Libraries**
- **Concepts**: Environment variables, hiding sensitive information.
- **Purpose**: Use the `dotenv` and `os` libraries to securely manage credentials.
- **Learning Points**:
  - Why it's unsafe to hardcode credentials.
  - How to use environment variables with `.env`.
- **Run**:
  ```bash
  python part2.py
  ```

---

### **Part 3: Sending Multiple Commands with a For Loop**
- **Concepts**: For loops, iterating over lists.
- **Purpose**: Send multiple commands to a single device.
- **Learning Points**:
  - What a for loop is and how it helps automate repetitive tasks.
- **Run**:
  ```bash
  python part3.py
  ```

---

### **Part 4: Nested For Loops for Multiple Devices**
- **Concepts**: Nested loops, interacting with multiple devices.
- **Purpose**: Execute multiple commands across multiple devices.
- **Learning Points**:
  - How to structure nested loops to iterate over multiple lists.
- **Run**:
  ```bash
  python part4.py
  ```

---

### **Part 5: Reading from Text and Writing to CSV**
- **Concepts**: File handling, CSV files.
- **Purpose**: Read device IPs from a text file and save results to a CSV file.
- **Learning Points**:
  - How to work with files using Python.
  - How to use the `csv` module for structured data storage.
- **Run**:
  ```bash
  python part5.py
  ```

---

### **Part 6: Input and Output via CSV Files**
- **Concepts**: Input/output management with CSV.
- **Purpose**: Use a CSV file to provide devices and commands and save outputs in the same format.
- **Learning Points**:
  - Structuring input data for complex automation tasks.
- **Run**:
  ```bash
  python part6.py
  ```

---

### **Part 7: Error Handling with Try-Except-Finally**
- **Concepts**: Error handling.
- **Purpose**: Ensure the script handles device failures gracefully.
- **Learning Points**:
  - What `try`, `except`, and `finally` blocks do and how to use them.
- **Run**:
  ```bash
  python part7.py
  ```

---

### **Part 8: Refactoring with Functions**
- **Concepts**: Modularization, reusability.
- **Purpose**: Break the script into reusable functions for better structure.
- **Learning Points**:
  - Why and how to use functions.
  - How to refactor existing code for clarity and maintainability.
- **Run**:
  ```bash
  python part8.py
  ```

---

### **Part 9: Efficiency with `concurrent.futures`**
- **Concepts**: Concurrency, threading.
- **Purpose**: Improve script efficiency by processing multiple devices simultaneously.
- **Learning Points**:
  - What `concurrent.futures` is and how to use it.
  - How threading boosts efficiency in I/O-bound tasks.
- **Run**:
  ```bash
  python part9.py
  ```

---

## **What You'll Learn**
By following this progression, you'll gain:
- Practical Python skills tailored for network automation.
- A deeper understanding of how to structure scripts for efficiency and scalability.
- Confidence to build your own tools for automating repetitive tasks in networking.

---

