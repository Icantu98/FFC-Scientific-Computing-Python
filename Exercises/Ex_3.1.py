hours = float(input('Hours worked: ')) #float > int for decimals
payRate = float(input('Payrate per hour:')) #float > int for decimals


if hours <= 40:
    pay = hours * payRate #normal pay
elif hours > 40:
    pay = (40 * payRate) + ((hours - 40)* (payRate*1.5)) #(normalpay) + (overtime pay) 
    print(hours-40,'hours of overtime')
else:
    print('Error')
print('Expect: $',pay)
