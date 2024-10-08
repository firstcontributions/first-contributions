#Define the menu of restaurant
menu = {
    'pizza':50,
    'pasta':60,
    'salad':90,
    'coffee':70,
    'burger':40,
}
#Great
print("Welcome to .PY Restaurant")
print("pizza: 50Rs\npasta: 60Rs\nsalad: 90Rs\ncoffee: 70Rs\nburger: 40Rs")

order_total =0
#90 + 70 = 160

item_1 = input("enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"you item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet !")

another_order = input("Do you want to add another item? (yes/No)")
if another_order == "yes":
    item_2 = input("enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f" The total amount of items to pay is {order_total}")
