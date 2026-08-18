class Food:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def display_items(self):
        print(f"item:{self.name} category:${self.category} price:{self.price}")


              
    
        