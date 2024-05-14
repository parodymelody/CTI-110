#Maurice Mccrimmon
#03/24/2024
#P3HW2
#Assignment assess student understanding of decision structures
#Psudeocode(detail algorithm)

name = input ("Enter employee's name: ")
workhours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employees payrate: "))
if workhours <= 40:
    regpay = (workhours * pay_rate)
    overtime_pay = 0
else:
    regpay = 40 * pay_rate
    oth = workhours - 40
    overtime_pay = oth * (pay_rate * 2.5)
gross_pay = regpay + overtime_pay


print("-----------------------------------------")
print("Employee name:", name)


print(f"Hours Worked\tPay Rate\tOvertime\tOvertime Pay      \tRegHour Pay       \tGross Pay")
print("----------------------------------------------------------------------------------------------------------")
print(f"{workhours:.1f}\t\t{pay_rate:.2f}   \t{oth:.1f}\t\t"
      f"${overtime_pay:.2f}'\t\t${regpay:.2f}\t\t${gross_pay:.2f}\n")
