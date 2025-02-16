from persistence import *
import sys

def process_action(action: list[str]):
    product_id = int(action[0])
    quantity = int(action[1])
    activator_id = int(action[2])
    date = action[3]

    # Get current product quantity
    product_data = repo.execute_command(f"SELECT quantity FROM products WHERE id={product_id};")
    if not product_data:
        return  # Ignore invalid product IDs

    current_quantity = product_data[0][0]

    # Sale (negative quantity)
    if quantity < 0:
        if current_quantity + quantity < 0:
            return  # Not enough stock, ignore action

    # Update product quantity
    new_quantity = current_quantity + quantity
    repo.execute_command(f"UPDATE products SET quantity={new_quantity} WHERE id={product_id};")

    # Insert into activities
    repo.execute_command(f"""
        INSERT INTO activities (product_id, quantity, activator_id, date)
        VALUES ({product_id}, {quantity}, {activator_id}, '{date}');
    """)
# Commit changes to ensure persistence
    repo._conn.commit()

def main(args : list[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            process_action(splittedline)

if __name__ == '__main__':
    main(sys.argv)