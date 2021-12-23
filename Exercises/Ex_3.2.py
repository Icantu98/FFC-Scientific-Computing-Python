hours = input('Hours worked: ') #float > int for decimals
payRate = input('Payrate per hour:') #float > int for decimals

try:
    hours = float(hours)
except:
    hours = -1
try:
    payRate = float(payRate)
except:
    payRate = -1
error = hours*payRate # error will always be negative if an error ensued

if error < 0:
    print('Error, please enter numeric input')
    exit()
elif hours <= 40:
    pay = hours * payRate #normal pay
elif hours > 40:
    pay = (40 * payRate) + ((hours - 40)* (payRate*1.5)) #(normalpay) + (overtime pay) 
    print(hours-40,'hours of overtime')

print('Expect: $',pay)