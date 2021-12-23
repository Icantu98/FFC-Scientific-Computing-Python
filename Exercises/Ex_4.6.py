hrs = input('Hours worked: ') #float > int for decimals
payR = input('Payrate per hour:') #float > int for decimals

try:
    hrs = float(hrs)
except:
    hrs = -1
try:
    payR = float(payR)
except:
    payR = -1
error = hrs*payR # error will always be negative if an error ensued

def computePay(hrs,payR):
    error = hrs * payR
    if (error) < 0:
        return 'Error, please enter numeric input'
    elif hrs <= 40:
        payOut = hrs * payR #normal pay
        return payOut
    elif hrs > 40:
        payOut = (40 * payR) + ((hrs - 40)* (payR*1.5)) #(normalpay) + (overtime pay) 
        return payOut

pay = computePay(hrs,payR)

print('Expect: $ ',pay)
