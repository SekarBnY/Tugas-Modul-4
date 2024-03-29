import tkinter as tk
from tkinter import messagebox

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, index):
        if 0 <= index < len(self.items):
            del self.items[index]
        else:
            messagebox.showerror("Error", "Invalid item index")

    def get_total_cost(self):
        return sum(item.price for item in self.items)

class Product:
    def __init__(self, number, name, price):
        self.number = number
        self.name = name
        self.price = price

def create_products():
    products = [
        Product(1, "Shoes", 50),
        Product(2, "T-shirt", 20),
        Product(3, "Jeans", 40),
        Product(4, "Hat", 15),
        Product(5, "Socks", 10),
        Product(6, "Jacket", 60),
        Product(7, "Pants", 30),
        Product(8, "Watch", 70),
        Product(9, "Backpack", 50),
        Product(10, "Belt", 20),
        Product(11, "Scarf", 15),
        Product(12, "Sunglasses", 30),
        Product(13, "Gloves", 25),
        Product(14, "Dress", 45),
        Product(15, "Sandals", 35),
        Product(16, "Skirt", 25),
        Product(17, "Sweater", 55),
        Product(18, "Boots", 65)
    ]
    return products

class ShoppingCartApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Shopping Cart")

        self.products = create_products()
        self.cart = ShoppingCart()
        self.cart_text = tk.Text(self.master, height=10, width=50)
        self.total_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Create labels and buttons for adding items
        for product in self.products:
            label_text = f"{product.number}. {product.name}: ${product.price:.2f}"
            label = tk.Label(self.master, text=label_text)
            label.grid(row=product.number, column=0, sticky="w")
            add_button = tk.Button(self.master, text="Add", command=lambda p=product: self.add_to_cart(p), bg="blue")
            add_button.grid(row=product.number, column=1)
            remove_button = tk.Button(self.master, text="Remove", command=self.remove_item, bg="red")
            remove_button.grid(row=product.number, column=2)

        # Create a text area for displaying the cart
        self.cart_text.grid(row=len(self.products) + 1, column=0, columnspan=3)

        # Create a label for displaying the total cost
        tk.Label(self.master, text="Total Cost:").grid(row=len(self.products) + 2, column=0)
        tk.Label(self.master, textvariable=self.total_text).grid(row=len(self.products) + 2, column=1)

        # Create a button for calculating the total cost
        tk.Button(self.master, text="Calculate Total", command=self.calculate_total, bg="green").grid(row=len(self.products) + 3, column=0, columnspan=2)

        # Create an entry and button for removing an item
        self.remove_index_entry = tk.Entry(self.master)
        self.remove_index_entry.grid(row=len(self.products) + 4, column=0)
        tk.Button(self.master, text="Remove Item", command=self.remove_item, bg="red").grid(row=len(self.products) + 4, column=1)

    def add_to_cart(self, product):
        self.cart.add_item(product)
        self.update_cart_text()

    def remove_item(self):
        try:
            index = int(self.remove_index_entry.get()) - 1
            self.cart.remove_item(index)
            self.update_cart_text()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid product number to remove.")

    def calculate_total(self):
        total_cost = self.cart.get_total_cost()
        self.total_text.set("${:.2f}".format(total_cost))

    def update_cart_text(self):
        self.cart_text.delete(1.0, tk.END)  # Clear the current text
        for item in self.cart.items:
            self.cart_text.insert(tk.END, f"{item.number}. {item.name}: ${item.price:.2f}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingCartApplication(root)
    root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    ShoppingCartGUI(root)
    root.mainloop()
