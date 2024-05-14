#Maurice Mccrimmon
#3/28/2024
#P4HW1
#Assignment assess student ability to edit and enhance exiting programs
Slist = []
score = int(input("How many scores do you want to enter? "))
for grade in range (score) :
    sc = int(input(f"Enter score{grade + 1}:"))
    while sc<0 or sc>100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        sc = int(input(f"Enter score again{grade + 1}:"))
    Slist.append (sc)
print(Slist)
avg = sum(Slist)/len(Slist)
print("--------results------------")
list_min = min(Slist)
print(f"Lowest Score: {list_min:.1f}")
print("Modifed List:", Slist)
print(f"Average:",avg) 
if avg >= 90:
 print("Your grade is: A")
 
elif avg >= 80:
 print("Your grade is: B")
elif avg >= 70:
 print("Your grade is: C")
elif avg >= 60:
 print("Your grade is: D")
else:
 print("Your grade is: F")
