num = 0 #running count
tot = 0 #running total

while True:
    str_val = input('Enter a number: ')
    if str_val == 'done':
        break
    try:
        flo_val = float(str_val)
    except:
        print('Invalid Input')
        continue #go back up to the top of the loop
    num = num + 1
    tot = tot + flo_val

print('All Done')
print(tot,num,tot/num)