Total_cost = int(input("Enter the total cost of the items: "))
if Total_cost >= 1000:
    discount = Total_cost * 0.2
    print("You have received a 20% discount")
    Total_cost -= discount
    print("The total cost is now: ", Total_cost)
elif Total_cost >= 500:
    discount = Total_cost * 0.1
    print("You have received a 10% discount")
    Total_cost -= discount
    print("The total cost is now: ", Total_cost)
elif Total_cost >= 100:
    discount = Total_cost * 0.05
    print("You have received a 5% discount")
    Total_cost -= discount
    print("The total cost is now: ", Total_cost)
else:
    print("You have not received a discount")
    print("The total cost is: ", Total_cost)