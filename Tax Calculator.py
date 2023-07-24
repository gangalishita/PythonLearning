# Items purchased
item_1_name = "Milk Carton"
item_1_cost = 2.79
item_1_amount = 2

item_2_name = "Bread"
item_2_cost = 1.55
item_2_amount = 1

# Total costs before tax
item_1_total_cost = item_1_cost * item_1_amount
item_2_total_cost = item_2_cost * item_2_amount
TotalCostBeforeTax = item_1_total_cost + item_2_total_cost

# Sales tax percent
tax = 7.5

# Total cost after tax
TotalCost_AfterTax = TotalCostBeforeTax + (TotalCostBeforeTax * tax * 0.01)

# Printed Receipt
print(" ")
print("Receipt")
print(" ")
print("Item: " + item_1_name)
print("Cost: $" + str(item_1_cost))
print("Number Purchased: " + str(item_1_amount))
print("-------------")
print("Item: " + item_2_name)
print("Cost: $" + str(item_2_cost))
print("Number Purchased: " + str(item_2_amount))
print("-------------")
print("Subtotal: " + str(TotalCostBeforeTax))
print("Sales Tax: " + str(tax) + "%")
print("Total Cost After Tax: $ " + str(TotalCost_AfterTax))
print(" ")
