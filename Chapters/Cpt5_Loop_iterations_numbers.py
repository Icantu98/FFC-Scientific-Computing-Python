nums = [9, 41, 12, 3, 74, 15]

# how to count things in a list
count  = 0
print('Before', count)
for item in nums:
    count = count + 1
    print(count,item)
print('After', count)

# Running total in list loop
x = 0
print('Before',x)
for item in nums:
    x = x + item
    print(x,item)
print('After', x)

# Average loop
count = 0
x = 0
print('Before', count, sum)
for item in nums:
    count = count + 1
    x = x + item
    print(count, x, item)
print('Average', x/count)

#Filtering in a loop
print('Before')
for item in nums:
    if item > 20:
        print('Large Number', item)
print('Done')

#Boolean Variable in a loop
found = False
print('Before', found)
for item in nums:
    if item == 3:
        found = True
    print(found,item)
    found = False
print('After', found)

#how to find smallest value
smallest = None # use "None" as starting value cause its means empty to start with
print('Before', None)
for item in nums:
    if smallest is None: # use None value to then set base number something from the data set
        smallest = item
    elif item < smallest:
        smallest = item
    print(smallest, item)
print('After', smallest)




