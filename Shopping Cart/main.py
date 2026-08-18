"""What to build
Build a basic E-Commerce Shopping Cart System using OOP.

Create a Product class containing information such as

Product ID

Product Name

Category

Price

Available Stock

Create another class called ShoppingCart.

The shopping cart should allow a user to add products, remove products, display selected products, calculate the total amount, and check whether a product is available.

Create at least 5 different products and demonstrate a customer purchasing multiple products.

The program should also handle a simple situation where a product cannot be purchased if its stock is zero."""


from product import Product
from shopping_cart import shoppingCart

if __name__ == "__main__":

    # Creating 5 electronic product models
    laptop = Product(101, "Dell Inspiron 15", "Laptop", 799.99, 10)
    mouse = Product(102, "Logitech MX Master 3", "Mouse", 99.99, 25)
    keyboard = Product(103, "Mechanical Keyboard Pro", "Keyboard", 149.99, 15)
    headphones = Product(104, "Sony WH-1000XM5", "Headphones", 349.99, 8)
    monitor = Product(105, "Samsung 27inch 4K Monitor", "Monitor", 499.99, 5)

    print("========== AVAILABLE PRODUCTS ==========")

    laptop.display()
    headphones.display()
    keyboard.display()
    mouse.display()
    monitor.display()



    cart = shoppingCart()

    cart.add_product(laptop)
    cart.add_product(headphones)
    cart.add_product(keyboard)
    cart.add_product(mouse)

    cart.display_cart()
    cart.display_total()
    cart.remove_product(keyboard)

    cart.display_cart()
    cart.display_total()


