
inventory = {}
print(inventory)
for _ in range(3):
    product_name = input("Enter the product name: ")
    quantity = int(input(f"Enter the quantity for {product_name}: "))
    inventory[product_name] = quantity


product_name = input("Enter the product name to sell: ")
quantity_sold = int(input(f"Enter the quantity to sell for {product_name}: "))

if product_name in inventory:
    if inventory[product_name] >= quantity_sold:
        inventory[product_name] -= quantity_sold
        print(f"Sold {quantity_sold} of {product_name}. You have rn: {inventory[product_name]}")
    else:
        print(f"You dont have enough {product_name}. you have rn: {inventory[product_name]}")
else:
    print(f"Product {product_name} does not exist in the inventory.")

print(inventory)