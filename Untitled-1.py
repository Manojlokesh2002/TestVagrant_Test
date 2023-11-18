class Product:
    def _init_(self, name, unit_price, quantity=1, gst_eligible=False):
        self.name, self.unit_price, self.quantity, self.gst_eligible = name, unit_price, quantity, gst_eligible

class ShoppingCart:
    def _init_(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total_amount(self):
        return sum(p.unit_price * p.quantity for p in self.products)

    def identify_max_gst_product(self):
        return max((p for p in self.products if p.gst_eligible), key=lambda x: x.unit_price * x.quantity)

# Creating products and shopping cart
cart = ShoppingCart()
cart.add_product(Product("Loather Wallot", 1100, 1, True))
cart.add_product(Product("Umbrella", 900, 12, True))
cart.add_product(Product("Notebook", 200, 28))
cart.add_product(Product("Honey", 100))

# Getting results
max_gst_product = cart.identify_max_gst_product()
total_amount_to_pay = cart.calculate_total_amount()

# Printing results
print(f"Product with Maximum GST Amount: {max_gst_product.name}")
print(f"Total Amount to be Paid: Rs. {total_amount⬤