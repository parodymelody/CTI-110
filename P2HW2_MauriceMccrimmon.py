#Maurice Mccrimmon
#3/8/2024
#P2HW2 
#Brief description of program

nums = []

#Get grades from user
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

nums.append(mod1)
nums.append(mod2)
nums.append(mod3)
nums.append(mod4)
nums.append(mod5)
nums.append(mod6)



print("----------Results=---------")

list_min = min(nums)
print(f"Lowest Grade: {list_min:.1f}")
list_max = max(nums)
print(f"Highest Grade: {list_min:.1f}")
list_sum = sum(nums)
print(f"Sum of Grades: {list_sum:.1f}")
average = (mod1 + mod2 + mod3 + mod4 + mod5 + mod6) / 6
print(f"Average: {average:.2f}")
