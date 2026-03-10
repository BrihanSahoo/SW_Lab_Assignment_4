
import csv
import os

INVENTORY_FILE = "inventory.csv"

purchase_history = []

def initialize_inventory():
    if not os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ProductID", "ProductName", "Price", "Quantity"])


def add_product():
    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))

    with open(INVENTORY_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([product_id, name, price, quantity])

    print("Product added successfully!\n")


def view_inventory():
    with open(INVENTORY_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()


def purchase_product():
    product_id = input("Enter Product ID to purchase: ")
    quantity_needed = int(input("Enter Quantity: "))

    updated_rows = []
    found = False

    with open(INVENTORY_FILE, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        updated_rows.append(header)

        for row in reader:
            if row[0] == product_id:
                found = True
                available_qty = int(row[3])

                if available_qty >= quantity_needed:
                    row[3] = str(available_qty - quantity_needed)
                    purchase_history.append([product_id, row[1], quantity_needed])
                    print("Purchase successful!")
                else:
                    print("Not enough stock!")

            updated_rows.append(row)

    if not found:
        print("Product not found!")

    with open(INVENTORY_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)


def view_purchase_history():
    print("\nPurchase History:")
    for purchase in purchase_history:
        print(purchase)
    print()


def main():
    initialize_inventory()

    while True:
        print("1. Add Product (Seller)")
        print("2. View Inventory")
        print("3. Purchase Product (Customer)")
        print("4. View Purchase History")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            purchase_product()
        elif choice == '4':
            view_purchase_history()
        elif choice == '5':
            break
        else:
            print("Invalid choice!\n")


if __name__ == "__main__":
    main()
