"""
What to build
Build a small Online Food Ordering System using OOP.
Create appropriate classes to represent a restaurant, food items, customers, and orders. Your program should allow you to create food items with a name, category, and price; create a customer; add multiple food items to an order; calculate the total bill; and display the complete order summary.
Create at least 5 food items and demonstrate at least 2 different customer orders.

"""
import sys
from food import Food
from customer import Customer
from order import order
from restaurant import Restaurant

if __name__ == "__main__":
    rest1  = Restaurant("Food Paradise")
    pizza = Food("Pizza", "Main Course", 250)
    burger = Food("Burger", "Fast Food", 150)
    biryani = Food("Chicken Biryani", "Main Course", 220)
    pasta = Food("Pasta", "Main Course", 180)
    ice_cream = Food("Ice Cream", "Dessert", 100)

    rest1.add_food_item(pizza)
    rest1.add_food_item(burger)
    rest1.add_food_item(biryani)
    rest1.add_food_item(pasta)
    rest1.add_food_item(ice_cream)

    rest1.display_menu()


    rest2  = Restaurant("Food choice")
    pizza1 = Food("Pizza", "Main Course", 250)
    burger1 = Food("chinise noodle", "Fast Food", 150)
    biryani1 = Food("Mutton Biryani", "Main Course", 220)
    pasta1 = Food("Pasta", "Main Course", 180)
    ice_cream1 = Food("Ice Cream", "Dessert", 100)
    
    rest2.add_food_item(pizza1)
    rest2.add_food_item(burger1)
    rest2.add_food_item(biryani1)
    rest2.add_food_item(pasta1)
    rest2.add_food_item(ice_cream1)
    
    rest2.display_menu()



    customer1 = Customer(101, "Rahul")
    customer2 = Customer(102, "Aisha")

    order1 = order(1001, customer1)

    order1.add_item(pizza)
    order1.add_item(burger)
    order1.add_item(ice_cream)


    order2 = order(1001, customer2)
    
    order2.add_item(pizza1)
    order2.add_item(burger1)
    

    order1.display_order()

    order2.display_order()


