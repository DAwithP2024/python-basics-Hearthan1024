

# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    sorted_products = sorted(products_list, key=lambda x: x[1], reverse=(sort_order == 2))
    display_products(sorted_products)
    return sorted_products


def display_products(products_list):
    for i, (product, price) in enumerate(products_list, 1):
        print(f"{i}. {product} - ${price}")


def display_categories():
    for i, category in enumerate(products.keys(), 1):
        print(f"{i}. {category}")
    try:
        category_choice = int(input("Select a category by number: "))
        if 1 <= category_choice <= len(products):
            return category_choice - 1
        else:
            print("Invalid choice. Please select a valid category number.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None
        


def add_to_cart(cart, product, quantity):
    cart.append((product, quantity))

def display_cart(cart):
    for product, quantity in cart:
        print(f"{product} - Quantity: {quantity}")


def generate_receipt(name, email, cart, total_cost, address):
     print("\nReceipt")
     print("-------")
     print(f"Name: {name}")
     print(f"Email: {email}")
     print(f"Address: {address}")
     print("\nItems Purchased:")
     for product, quantity in cart:
        print(f"{product} - Quantity: {quantity}")
     print(f"\nTotal Cost: ${total_cost}")
     print("\nYour order will be delivered in 3 days. Payment will be charged after the delivery is successful.")

def validate_name(name):
    parts = name.split()
    if len(parts) != 2:
        return False
    for part in parts:
        if not part.isalpha():
            return False
    return True


def validate_email(email):
    return "@" in email


def main():
    cart = []
    total_cost = 0

    name = input("Enter your name: ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid first and last name.")
        name = input("Enter your name: ")

    email = input("Enter your email: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email address.")
        email = input("Enter your email: ")

    while True:
        print("\nCategories:")
        display_categories()
        category_index = display_categories()
        if category_index is None:
            continue

        category = list(products.keys())[category_index]
        print(f"\nProducts in {category}:")
        display_products(products[category])

        while True:
            print("\nOptions:")
            print("1. Select a product to buy")
            print("2. Sort the products according to the price")
            print("3. Go back to the category selection")
            print("4. Finish shopping")
            option = int(input("Select an option: "))

            if option == 1:
                product_choice = int(input("Enter the product number: "))
                if product_choice < 1 or product_choice > len(products[category]):
                    print("Invalid choice. Please select a valid product number.")
                    continue
                product = products[category][product_choice - 1]
                quantity = int(input("Enter the quantity: "))
                add_to_cart(cart, product[0], quantity)
                total_cost += product[1] * quantity
            elif option == 2:
                sort_order = int(input("Sort by price: 1 for ascending, 2 for descending: "))
                sorted_products = display_sorted_products(products[category], sort_order)
                display_products(sorted_products)
            elif option == 3:
                break
            elif option == 4:
                if cart:
                    print("\nYour Cart:")
                    display_cart(cart)
                    print(f"\nTotal Cost: ${total_cost}")
                    address = input("Enter your delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using ourr portal. Hope you buy something from us next time. Have a nice day!")
                return
            else:
                print("Invalid option. Please select a valid option.")
if __name__ == "__main__":
    main()
