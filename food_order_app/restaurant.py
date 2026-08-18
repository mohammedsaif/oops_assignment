from food  import Food
class Restaurant():
    def __init__(self,name):
        self.name= name;
        self.menu = [];
    def add_food_item(self, food_item):
        self.menu.append(food_item)

    def display_menu(self):
        print(f"\n===== {self.name} MENU =====")

        for item in self.menu:
            item.display_items()


        