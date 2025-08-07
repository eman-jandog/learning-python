class User:
    def __init__(self, name, cart):
        self.name = name
        self.cart = cart

class Products:
    def __init__(self):
        self.products = []

    def __str__(self):
        display = "Product Listing: \n"
        if len(self.products) == 0:
            display += "\nNo available products."
        else:
            products = ''
            for product in self.products:
                products += f'{product.name} - P{product.price} - x{product.quantity}\n'
            display += products
    
    def add(self, item):
        if isinstance(item, ProductItem):
            
            self.products.append(item)
            return "Added Succesfully"
        else:
            raise ValueError("item is not a product")


class ProductItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return self.name

class Cart:
    def __init__(self, items=None):
        if items is None:
            self.items = []
        elif isinstance(items, list):
            self.items = items
        else:
            raise ValueError("items must be list.")

    def add(self, item):
        if isinstance(item, ProductItem):
            self.items.append(item)
            return "Added Succesfully"
        else:
            raise ValueError("item is not a product")
    



