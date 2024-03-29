class ShoppingCart:
    def __init__(self):
        self.items = []

    # Method (non-return type) untuk meletakkan barang di keranjang
    def add_item(self, item):
        self.items.append(item)
        print(f"{item} added to cart.")

    # Method (non-return type) untuk display barang di keranjang
    def display_cart(self):
        if self.items:
            print("Items in your cart:")
            for item in self.items:
                print("-", item)
        else:
            print("Your cart is empty.")

    # Method (non-return type) untuk mengkalkulasi total cost
    def calculate_total(self):
        total_cost = 0
        for item in self.items:
            total_cost += item.price
        return total_cost

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Function with return type untuk membuat produk
def create_products():
    products = [
        Product("Shoes", 50),
        Product("T-shirt", 20),
        Product("Jeans", 40),
        Product("Hat", 15),
        Product("Socks", 10)
    ]
    return products

# Main program
if __name__ == "__main__":
    # Create products
    products = create_products()

    # Initialize shopping cart
    cart = ShoppingCart()

    # Display available products
    print("Available products:")
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product.name} - ${product.price}")

    # User interaction to add items to the cart
    while True:
        choice = input("Enter the number of the product you want to add to cart (0 to exit): ")
        if choice == '0':
            break
        elif choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(products):
                cart.add_item(products[choice - 1].name)
            else:
                print("Invalid choice. Please enter a valid product number.")
        else:
            print("Invalid input. Please enter a valid product number.")

    # Display items in the cart
    cart.display_cart()

    # Calculate and display total cost
    total_cost = cart.calculate_total()
    print(f"Total cost of your purchases: ${total_cost}")
