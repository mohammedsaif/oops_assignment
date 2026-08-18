class shoppingCart:
    def __init__(self):
        self.items = []

     # Add product to cart
    def add_product(self, product):

        if product.check_availability():

            self.items.append(product)

            # Reduce stock after purchase
            product.stock -= 1

            print(f"{product.product_name} added to cart.")

        else:
            print(f"Sorry! {product.product_name} is out of stock.")

    # Remove product from cart
    def remove_product(self, product):
        if product in self.items:
            self.items.remove(product)
            product.stock += 1
            print(f"{product.product_name} removed from cart.")
        else:
            print(f"{product.product_name} is not in the cart.")

    def display_cart(self):
        print("\n========== SHOPPING CART ==========")
        if len(self.items) == 0:
            print("cart is empty : ")
            return
        for product in self.items:



                        print(
                f"{product.product_name} - "
                f"₹{product.price}"
            )
    def calculate_total(self):
        print("\n=============TOTAL BILL ==============")
        total = 0

        for product in self.items:
            total += product.price

        return total

    def display_total(self):

        print("-----------------------------------")
        print(f"Total Amount: ₹{self.calculate_total()}")
       
       