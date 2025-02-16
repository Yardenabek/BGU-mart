from persistence import *

def print_table(table_name, order_by="id"):
    """Prints a table's name followed by its records sorted by a given column."""
    print(table_name)
    rows = repo.execute_command(f"SELECT * FROM {table_name} ORDER BY {order_by}")
    for row in rows:
        print(row)
    print()

def print_activities():
    """Prints the detailed activities report sorted by date."""
    rows = repo.execute_command("""
        SELECT activities.date, products.description, activities.quantity, 
               employees.name, suppliers.name
        FROM activities
        LEFT JOIN products ON activities.product_id = products.id
        LEFT JOIN employees ON activities.activator_id = employees.id
        LEFT JOIN suppliers ON activities.activator_id = suppliers.id
        ORDER BY activities.date
    """)
    
    if rows:
        print("Activities report")
        for row in rows:
            # Replace None values for proper display
            formatted_row = tuple("None" if value is None else value for value in row)
            print(formatted_row)
        print()

def print_employees_report():
    """Prints the detailed employees report in ascending order of name."""
    rows = repo.execute_command("""
        SELECT employees.name, employees.salary, branches.location,
               COALESCE(SUM(products.price * ABS(activities.quantity)), 0)
        FROM employees
        JOIN branches ON employees.branche = branches.id
        LEFT JOIN activities ON employees.id = activities.activator_id
        LEFT JOIN products ON activities.product_id = products.id
        GROUP BY employees.id
        ORDER BY employees.name
    """)

    print("Employees report")
    for row in rows:
        print(" ".join(str(value) for value in row))
    print()

def main():
    # First, print tables in ascending order as required
    print_table("activities", order_by="date")
    print_table("branches")
    print_table("employees")
    print_table("products")
    print_table("suppliers")

    # Then print the reports
    print_employees_report()
    print_activities()

if __name__ == '__main__':
    main()
