# ex of a collection
friends = ['Joseph','Glenn','Sally']
print(friends[1]) # Prints Glenn   

for person in friends:
    print('Merry Christmas',person)

#lists are mutable
numbers = [1,2,3,4,5]
numbers[2] = 9 #change index 2 in list to 9
print(numbers)

#range
print(len(friends))
print(range(len(friends)))

#loops through range instead of length
for i in range(len(friends)):
    friend = friends[i]
    print('Happy new year',friend)

###########################
# Operations of lists

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c) #prints a combined list of a and b

#slicing lists
t = [9,41,12,3,74,15]
print(t[1:3])
print(t[:5])

#list Methods
stuff = list() #makes an empty list
stuff.append('book') #adds book to list
stuff.append('99')
print(stuff)

some = [1,2,3,4,5]
3 in some # returns true
print(max(some))
print(sum(some))

friends.sort() # sorts list in alphabetical order
print(friends)
 
numlist = list()
while True:
    inp = input('Enter a number : ')
    if inp == 'done':
        break
    finp = float(inp)
    numlist.append(finp)
average = sum(numlist)/len(numlist)
print("Average is: ",average)



