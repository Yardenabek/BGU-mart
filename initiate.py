from persistence import *

import sys
import os

def add_branche(splittedline: list[str]):
    branch = Branche(id=int(splittedline[0]), location=splittedline[1], number_of_employees=int(splittedline[2]))
    repo.execute_command(f"INSERT INTO branches (id, location, number_of_employees) VALUES ({branch.id}, '{branch.location}', {branch.number_of_employees});")
    repo._conn.commit()

def add_supplier(splittedline: list[str]):
    supplier = Supplier(id=int(splittedline[0]), name=splittedline[1], contact_information=splittedline[2])
    repo.execute_command(f"INSERT INTO suppliers (id, name, contact_information) VALUES ({supplier.id}, '{supplier.name}', '{supplier.contact_information}');")
    repo._conn.commit()

def add_product(splittedline: list[str]):
    product = Product(id=int(splittedline[0]), description=splittedline[1], price=float(splittedline[2]), quantity=int(splittedline[3]))
    repo.execute_command(f"INSERT INTO products (id, description, price, quantity) VALUES ({product.id}, '{product.description}', {product.price}, {product.quantity});")
    repo._conn.commit()

def add_employee(splittedline: list[str]):
    employee = Employee(id=int(splittedline[0]), name=splittedline[1], salary=float(splittedline[2]), branche=int(splittedline[3]))
    repo.execute_command(f"INSERT INTO employees (id, name, salary, branche) VALUES ({employee.id}, '{employee.name}', {employee.salary}, {employee.branche});")
    repo._conn.commit()

def add_activitie(splittedline: list[str]):
    activitie = Activitie(product_id=int(splittedline[0]), quantity=int(splittedline[1]), activator_id=int(splittedline[2]), date=splittedline[3])
    repo.execute_command(f"INSERT INTO activities (product_id, quantity, activator_id, date) VALUES ({activitie.product_id}, {activitie.quantity}, {activitie.activator_id}, '{activitie.date}');")
    repo._conn.commit()

adders = {  "B": add_branche,
            "S": add_supplier,
            "P": add_product,
            "E": add_employee}

def main(args : list[str]):
    inputfilename = args[1]
    # delete the database file if it exists
    repo._close()
    if os.path.isfile("bgumart.db"):
        os.remove("bgumart.db")
    repo.__init__()
    repo.create_tables()
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(",")
            adders.get(splittedline[0])(splittedline[1:])

if __name__ == '__main__':
    main(sys.argv)