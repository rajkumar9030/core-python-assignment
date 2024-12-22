menu = ["Pizza", "Burger", "Pasta", "Salad"]

def add_item(item):
    menu.append(item)

def remove_item(item):
    if item in menu:
        menu.remove(item)

def check_item(item):
    if item in menu:
        print(f"{item} is available")
    else:
        print(f"{item} is not available")

add_item("Tacos")
remove_item("Salad")
check_item("Pizza")

print("Updated menu:", menu)
