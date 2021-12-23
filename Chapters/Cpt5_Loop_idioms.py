# Looping through a set
print('Before')
for thing in [9,41,12,3,74,15]:
    print(thing)       #runs loop 6 times cause 6 items in list
print('After')

# Loop to find biggest number
numList = [4,42,564,234,6,45,324]
x = 0 # Set comparison variable to start with
for n in numList:
    if n > x: # if number is larger than x 
        x = n   # store it in x and move to next number
        print('Largest:',x,'Current:',n)
    elif n <= x: #if number is same or less than doesnt matter go next
        print('Largest:',x,'Current:',n)
        continue
    else:       #if anything else happens end the loop
        break
print('Largest number is', x) #display number stored


# Loop to find smallest number
smallest = None
print("Before:", smallest)
for n in [3, 41, 12, 9, 74, 15]:
    if smallest is None or n < smallest:
        smallest = n
    print("Loop:", n, smallest)
print("Smallest:", smallest)