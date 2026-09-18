class Product:
    current_id = 0 # class attribute
    def __init__(self, description, price): #instance method
        self.description = description
        self.id = Product.current_id
        Product.current_id += 1
        self.price = price

    def __str__(self):
        return f"Product {self.id}: {self.description} - ${self.price:.2f}"

ps = [Product("thinkpad", 1299.95), Product("mac", 3299.95)]
print(ps[1])
