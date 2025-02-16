# BGU Mart - Supermarket Management System

## Overview
BGU Mart is a simple supermarket management system implemented in Python using SQLite. It allows managing branches, employees, suppliers, products, and transactions efficiently. The system supports initializing the database, processing sales and supply transactions, and generating reports.

## Project Structure
The project consists of the following modules:

- **`persistence.py`**: Defines the data models and manages database connectivity.
- **`dbtools.py`**: Provides utility functions for handling database operations.
- **`initiate.py`**: Initializes the database and loads initial data from a file.
- **`action.py`**: Processes transactions, including sales and supply actions.
- **`printdb.py`**: Prints the database tables and generates reports.

## Installation
1. Ensure you have Python installed (>=3.7).
2. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/bgumart.git
   cd bgumart
   ```
3. Install dependencies (if any). Currently, the project only requires SQLite, which is built into Python.

## Usage
### 1. Initialize the Database
Run the following command to create the database and populate it with initial data:
```sh
python initiate.py <init_file>
```
Replace `<init_file>` with the path to the initialization file.

### 2. Process Transactions
Execute the following command to process sales and supply transactions:
```sh
python action.py <action_file>
```
Replace `<action_file>` with the path to the transactions file.

### 3. Print Reports
Generate reports by running:
```sh
python printdb.py
```
This will print the current state of all tables and display reports summarizing activities and employee performance.

## Database Schema
The database consists of the following tables:
- **`employees`**: Stores employee details, including salary and assigned branch.
- **`suppliers`**: Contains supplier information.
- **`products`**: Lists available products along with their prices and stock levels.
- **`branches`**: Represents supermarket branches.
- **`activities`**: Records product transactions, including sales and restocking.

## Example
### Initialization File (`init.txt`)
```
B,1,New York,10
E,101,John Doe,5000,1
P,201,Milk,2.5,100
S,301,FreshFarm,contact@freshfarm.com
```

### Transactions File (`actions.txt`)
```
201,-5,101,2025-02-16
201,10,301,2025-02-17
```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch.
3. Implement your changes and test thoroughly.
4. Submit a pull request.

## License
This project is licensed under the MIT License.

## Author
BGU Mart Project - Developed for educational purposes.

