# This program calculates an employee's take home pay.


salary = 1250.00
numDependents = 2

stateTax = salary * 0.065

print(f"State Tax: ${stateTax:.2f}")

federalTax = salary * 0.28

print(f"Federal Tax: ${federalTax:.2f}")

dependentDeduction = salary * (numDependents * 0.025)

print(f"Dependents: ${dependentDeduction:.2f}")

totalWithholding = stateTax + federalTax

print(f"Total withholding ${totalWithholding:.2f}")


takeHomePay = salary - totalWithholding + dependentDeduction

print(f"Salary: ${salary:.2f}")
print(f"Take-Home Pay: ${takeHomePay:.2f}")
