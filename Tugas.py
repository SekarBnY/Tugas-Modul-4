import tkinter as tk

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, index):
        if 0 <= index < len(self.items):
            return self.items.pop(index)
        else:
            print(f"Invalid index: {index}")

    def get_total_price(self):
        return sum(item.price for item in self.items)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def create_products():
    return [
        Product("Shoes", 50),
        Product("T-shirt", 20),
        Product("Jeans", 40),
        Product("Hat", 15),
        Product("Socks", 10)
    ]

class ShoppingCartGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Shopping Cart")

        self.products = create_products()
        self.cart = ShoppingCart()
        self.cart_text = tk.StringVar()
        self.total_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        for i, product in enumerate(self.products):
            tk.Label(self.root, text=f"{i+1}. {product.name} (${product.price})").grid(row=i, column=0)
            tk.Button(self.root, text="Add to Cart", command=lambda p=product: self.add_to_cart(p)).grid(row=i, column=1)

        tk.Label(self.root, textvariable=self.cart_text).grid(row=len(self.products)+1, column=0, columnspan=2)
        tk.Label(self.root, textvariable=self.total_text).grid(row=len(self.products)+2, column=1, sticky="w")

        tk.Button(self.root, text="Calculate Total", command=self.calculate_total).grid(row=len(self.products)+3, column=0, columnspan=2)

    def add_to_cart(self, product):
        self.cart.add_item(product)
        self.cart_text.set("Cart:\n" + "\n".join(item.name for item in self.cart.items))

    def calculate_total(self):
        total_price = self.cart.get_total_price()
        self.total_text.set(f"Total: ${total_price:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    ShoppingCartGUI(root)
    root.mainloop()
