class order:
     def __init__(self, order_id, customer):
            self.order_id = order_id
            self.customer = customer
            self.items = []

     def add_item(self, food_item):
        self.items.append(food_item)


     def calculate_total(self):
        total = 0

        for item in self.items:
            total += item.price

        return total

     def display_order(self):

        print("\n==============================")
        print(f"Order ID: {self.order_id}")

        self.customer.display_customer()

        print("\nOrdered Items:")

        for item in self.items:
            print(f"- {item.name} - ₹{item.price}")

        print("------------------------------")
        print(f"Total Bill: ₹{self.calculate_total()}")
        print("==============================")

        