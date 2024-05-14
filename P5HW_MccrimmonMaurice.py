#Maurice Mccrimmon
#4/23/2024
#P5HW
#Use of loops, functions and module import to complete assignments
import random

#Generate random numbers
def numsum():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(num1 ,"+", num2)
    numg = 1
    uguess = int(input("Enter Answer:"))
    numsum = (num1 + num2)
    while numsum != uguess:
        if numsum>uguess:
            print("Sorry, guess is too low.")
        if numsum<uguess:
            print("Sorry, guess is too high.")
        uguess = int(input("Try again:"))
        numg += 1            
    print("Congratulations!!! You got it correct")
    print("number of guesses:", numg)     
        
    
def numsub():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(num1 ,"-", num2)
    numg = 1
    uguess = int(input("Enter Answer:"))
    numsub = (num1 - num2)
    while numsub != uguess:
        if numsub>uguess:
            print("Sorry, guess is too low.")
        if numsub<uguess:
            print("Sorry, guess is too high.")
        uguess = int(input("Try again:"))
        numg += 1            
    print("Congratulations!!! You got it correct")
    print("number of guesses:", numg)     
        
    

def main():
    print("Welcome to Math Quiz")
    print("MAIN MENU")
    print("--------------------")

    #Menu driven program
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")

        
    option = input("Please choose one of the menu option: ")
    while option !="3":
        if option == "1":
            numsum()
        elif option == "2":
            numsub()
        else:
            print("Invalid Option")
        option = input("Please choose one of the menu option: ")
    print("Thank you for playing...")
    print("Goodbye!")
main()
       

