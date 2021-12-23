purse = dict()  # makes empy dictinary

# assing a 'label' and a value in the dictionary
purse['money'] = 12
purse['candy'] = 3
purse['tissue'] = 75

print(purse)
print(purse['candy'])

purse['candy'] = purse['candy'] + 5
print(purse['candy'])

purse['tissue'] = 69
print(purse)

purse[1] = 4 # you can use numbers as lables too
print(purse)

ooo = {}   # Different ay of making an empty dictionary
ooo['Ticker'] = 'SPY'
print(ooo)