
#Maurice Mccrimmon
#3/3/2024
#P2LAB1 - Math expressions aqnd f-strings

mpg = float(input("Enter the car's mpg: "))

cost_gas = float(input("How much is a gallon of gas: "))


miles_20 = (20/mpg) * cost_gas

miles_75 = (75/mpg) * cost_gas

miles_500 = (500/mpg) * cost_gas

print(f"Cost to drive 20 miles is ${miles_20:.2f}")


print(f"Cost to drive 75 miles is ${miles_75:.2f}")

print(f"Cost to drive 500 miles is ${miles_500:.2f}")
