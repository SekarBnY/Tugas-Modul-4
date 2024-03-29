class ShoppingCart:
    def __init__(self):
        self.items = []

    # Method untuk menambahkan barang ke keranjang
    def add_item(self, item):
        self.items.append(item)
        print(f"{item.name} ditambahkan ke keranjang.")

    # Method untuk menampilkan barang di keranjang
    def display_cart(self):
        if self.items:
            print("Barang dalam keranjang Anda:")
            for item in self.items:
                print("-", item.name)
        else:
            print("Keranjang Anda kosong.")

    # Method untuk menghitung total biaya
    def calculate_total(self):
        total_cost = sum(item.price for item in self.items)
        return total_cost

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Fungsi untuk membuat produk
def create_products():
    products = [
        Product("Sepatu", 50),
        Product("Kaos", 20),
        Product("Celana Jeans", 40),
        Product("Topi", 15),
        Product("Kaus Kaki", 10)
    ]
    return products

# Program utama
if __name__ == "__main__":
    products = create_products()

    cart = ShoppingCart()

    print("Produk yang tersedia:")
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product.name} - ${product.price}")

    while True:
        choice = input("Masukkan nomor produk yang ingin Anda tambahkan ke keranjang (0 untuk keluar): ")
        if choice == '0':
            break
        elif choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(products):
                cart.add_item(products[choice - 1])
            else:
                print("Pilihan tidak valid. Harap masukkan nomor produk yang valid.")
        else:
            print("Input tidak valid. Harap masukkan nomor produk yang valid.")

    cart.display_cart()

    total_cost = cart.calculate_total()
    print(f"Total biaya pembelian Anda: ${total_cost}")
