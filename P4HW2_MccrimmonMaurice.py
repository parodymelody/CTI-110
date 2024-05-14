#Maurice Mccrimmon
#04/09/2024
#P4HW2
#Assignment assess student understanding of decision structures
#Psudeocode(detail algorithm)
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
total_employees = 0
overtime_hours = 0
empname = input ("Enter employee's name or 'done' to terminate: ")
while empname != 'Done':
    workhours = float(input(f"How many hours did {empname} work? "))
    pay_rate = float(input(f"What is {empname}'s payrate: "))
    if workhours <= 40:
        regpay = (workhours * pay_rate)
        overtime_pay = 0
        oth = 0
    else:
        regpay = 40 * pay_rate
        oth = workhours - 40
        overtime_pay = oth * (pay_rate * 1.5)
    gross_pay = regpay + overtime_pay
    total_employees += 1
    total_regular_pay += regpay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    print("-----------------------------------------")
    print("Employee name:", empname)
    print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'Overtime':<15}{'Overtime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
    print("----------------------------------------------------------------------------------------------------------")
    print(f"{workhours:<15}${pay_rate:<15}{oth:<15}${overtime_pay:<15}${regpay:<15}${gross_pay:<15}")
    empname = input ("Enter employee's name or 'done' to terminate: ")
print("Total number of employees entered:", total_employees)
print(f"Total amount paid for overtime: ${total_overtime_pay}")
print(f"Total amount paid in regular hours: ${total_regular_pay}")
print(f"Total amount paid in gross: ${total_gross_pay}")
