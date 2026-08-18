class Product:
    def __init__(self,product_id,product_name,category,price,stock):
        self.product_id = product_id;
        self.product_name = product_name
        self.category = category;
        self.price = price;
        self.stock = stock

    def display(self):
        print(f"ID: {self.product_id}")
        print(f"Name: {self.product_name}")
        print(f"Category: {self.category}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock}")



    def check_availability(self):
         return self.stock > 0
    

    
        