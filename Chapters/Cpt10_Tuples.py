#Function like lists but are immutable

x = ('Glenn','Sally','Joseph')
print(x[2])

y = (1,9,2) # () Make it a Tuple
print(y)    
print (max(y))

y = [1,9,2] # [] make it a list
y[2] = 4 
print(y)

# made immutable for efficency\speed. Used to only STORE and not edit data
# good for a temperary variable. Lists are used to build up
t = tuple()
dir(t) # Count and Index are all you can do

# Dual Tuple
(x,y) = (4,'fred')
print(y) # prints 'fred'   

(a,b) = (99,98)
print(a) # prints 99

#related to dictionaries
# Can store tuples in dictonaries
d = dict()  
d['csev'] = 2
d['swen'] = 4

for (k,v) in d.items():
    print(k,v)

#Will print a list of tuples
tups = d.items()
print(tups)

# Comparable
#Left most is most significant

(0,1,2) < (5,1,2) # will compare 0 and 5 and will stop if true. Thus rest are not compared
(0,1,9) < (0,3,4) # will return true cause 1<3
('Jones','Sally') < ('Jones','Sam') # will do a string comparason


