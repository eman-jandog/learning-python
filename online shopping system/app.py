import json
import os

class ProductItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def __str__(self):
        return f'{self.name} - P{self.price} - x{self.quantity}\n'
    
    def update(self):
        for key, item in self.__dict__.items():
            self.__dict__[key] = input(f'{key[0].upper() + key[1:]} (current: {item}): ') or item

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
                products += f'{product}'
            display += products
        return display
        
    def get(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None
    
    def add(self, name, price, quantity):
        if self.get(name):
            return "Item is already exists in the list."        
        item = ProductItem(name, price, quantity)
        self.products.append(item)
        return "Added Succesfully"
        
    def update(self, name):
        product = self.get(name)
        if not product:
            return "Product name not found."
        product.update()  
        
    def remove(self, name):
        product = self.get(name)
        if product:
            self.products.remove(product)
        else:
            return "Product name not found."        

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def __str__(self):
        return f'{self.product.name} - P{self.product.price} - x{self.quantity}'

    def update(self):
        self.quantity = input(f'Quantity (current: {self.quantity}): ') or self.quantity

class Cart:
    def __init__(self):
        self.cart = []

    def __str__(self):
        cart = ''
        for item in self.cart:
            cart += f'{item}\n'
        return cart

    def get(self, name):
        for item in self.cart:
            if item.product.name.lower() == name.lower():
                return item
        return None

    def add(self, product, quantity=1):
        if not isinstance(product, ProductItem):
            return 'Invalid product item.'
        
        item = self.get(product.name)
        if item:
            item.quantity += quantity
        else:
            item = CartItem(product, quantity)
            self.cart.append(item)

    def update(self, name):
        item = self.get(name)
        if not item:
            return 'Invalid item.'
        item.update()
            
    def remove(self, name):
        item = self.get(name)
        if item:
            self.cart.remove(item)
            return "Item is remove from cart"
        return "Invalid item."

class User:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def __str__(self):
        return f"Name: {self.name} \nCart: {self.cart}"

if __name__ == '__main__':
    # Populate products
    dirname = os.path.dirname(__file__)
    file = os.path.join(dirname, 'products.json')
    with open(file, 'r') as file:
        data = json.load(file)

    product_listing = Products()
    for item in data:
        product_listing.add(
            item['product'],
            item['price'],
            item['quantity']
        )

    print(product_listing)

    # Create user
    user = User('User1')
    
    print(user)

    granola = product_listing.get('Granola Cereal')
    miso = product_listing.get('Miso Soup Starter')
    tortilla = product_listing.get('Tortilla Chips')

    user.cart.add(miso, 3)
    user.cart.add(tortilla, 5)
    user.cart.add(granola)
    user.cart.add(miso, 3)

    print(user.cart)

    user.cart.update('Miso Soup Starter')
    print(user.cart)
    user.cart.remove('Miso Soup Starter')
    print(user.cart)