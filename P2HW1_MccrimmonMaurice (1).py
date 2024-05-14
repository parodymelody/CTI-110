 # Maurice Mccrimmon
 # 3/3/2024
 # P2LAB1 
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
print(f"Inital Budget: ${budget:.2f}")
print()
print(f"Fuel: ${fuel:.2f}")
print(f"Accomodation: ${hotel:.2f}")
print(f"Food: ${food:.2f}")
print()
print(f"Remaining Balance: ${budget - travel_expenses:.2f}")
 
