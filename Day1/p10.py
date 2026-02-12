cart = []

while True:
    print("\n---- CART MENU ----")
    print("1. Add Item")
    print("2. View All Items")
    print("3. Search Item")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item to add: ")
        cart.append(item)
        print(f"{item} added to cart.")

    elif choice == "2":
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            print("Items in Cart:")
            for i in cart:
                print(i)

    elif choice == "3":
        search_item = input("Enter item to search: ")
        if search_item in cart:
            print(f"{search_item} is in the cart.")
        else:
            print(f"{search_item} not found in cart.")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
