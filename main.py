import products
import store


# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
]

best_buy = store.Store(product_list)


def list_products(store_obj: store.Store):
    products_list = store_obj.get_all_products()
    if not products_list:
        print("No products in store.")
        return
    for idx, prod in enumerate(products_list, start=1):
        print(f"{idx}. {prod}")


def show_total_amount(store_obj: store.Store):
    print(f"Total amount in store: {store_obj.get_total_quantity()}")


def make_order(store_obj: store.Store):
    products_list = store_obj.get_all_products()
    if not products_list:
        print("No products available for order.")
        return

    list_products(store_obj)
    try:
        choice = int(input("Select product number: "))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid input.")
        return

    if choice < 1 or choice > len(products_list):
        print("No such product.")
        return

    product = products_list[choice - 1]
    try:
        total_price = store_obj.order([(product, quantity)])
        print(f"Order successful! Total price: {total_price}")
    except Exception as e:
        print(f"Order failed: {e}")


def start(store_obj: store.Store):
    while True:
        print("\nStore Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ").strip()

        if choice == "1":
            list_products(store_obj)
        elif choice == "2":
            show_total_amount(store_obj)
        elif choice == "3":
            make_order(store_obj)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    start(best_buy)
