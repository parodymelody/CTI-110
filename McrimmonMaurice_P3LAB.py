
#Maurice Mccrimmon
#3/14/2024
#M3LAB - Branching
#Get amount of change owed from user
change = int(input("Enter an amount of change as integer: "))
if change == 0:
    print("No change")
    
#Caculate the amount of each coin needed
#integer division - //

num_dollars = change // 100
change = change - (num_dollars*100)

num_quarters = change // 25
change = change - (num_quarters * 25)

num_dimes = change // 10
change = change - (num_dimes * 10)

num_nickels = change // 5
change = change - (num_nickels * 5)

num_pennies = change // 1

#Display coins owed

if num_dollars > 0:
    print(num_dollars, end = " ")
    if num_dollars == 1:
        print("Dollar")
    else:
        print("Dollars")

if num_quarters > 0:
    print(num_quarters, end = " ")
    if num_quarters == 1:
        print("Quarter")
    else:
        print("Quarters")

if num_dimes > 0:
    print(num_dimes, end = " ")
    if num_dimes == 1:
        print("Dime")
    else: #if num_dimes > 1
        print("Dimes")

if num_nickels > 0:
    print(num_nickels, end = " ")
    if num_nickels == 1:
        print("Nickel")
    else:
        print("Nickels")
        
if num_pennies > 0:
    print(num_pennies, end = " ")
    if num_pennies == 1:
        print("Penny")
    else:
        print("Pennies")


