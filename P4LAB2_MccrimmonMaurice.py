#Maurice Mccrimmon
#3/28/2024
#P4LAB2
#Using the range function
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

while num1> num2:
    print("First number must be smaller")
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))

print("you did it right!")

for number in range (num1, num2+1, 5):
    print(number)
