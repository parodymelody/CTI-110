 # Maurice Mccrimmon
 # 2/22/2024
 # P1HW2
 # Caculate budget for travel

print("This program caculates and displays travel expenses")

budget = int(input("Enter Budget:"))
print()
destination = input("Enter your travel destination: ")
print()
fuel = int(input("How much do you think you will spend on gas?"))
print()
hotel = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = int(input("Last, how much do you need for food? "))
print()
travel_expenses = hotel + fuel + food
print("----------Travel Expenses----------")
print("Location:", destination)
print("Inital Budget:", budget)
print()
print("Fuel:", fuel)
print("Accomodation:", hotel)
print("Food:", food)
print()
print("Remaining Balance:", budget - travel_expenses)
