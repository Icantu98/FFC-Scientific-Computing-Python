# Produce a list of Tuples from dic. Then sort the tuples

d = {'a':10,'b': 1,'c':20}
d.items()
print(sorted(d.items())) # accending order sorted by KEY (first one) without looking at the value

# Print out values nicely in order using sorted()
for k,v in sorted(d.items()):
    print(k,v)

## Sort by values not key

c = {'a':10,'c':20,'b': 1}
temp = list()
for k,v in c.items():
    temp.append((v,k)) # FlIPS they KEYS and VALUES to make use of sorted
print(temp)

temp = sorted(temp, reverse=True) # Sortst in DECENDING order
print(temp)

# Closed form
print(sorted([ (v,k) for k,v in c.items()], reverse=True))
