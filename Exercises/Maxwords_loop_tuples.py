name = input('Enter file name: ')
try:
    fhand = open(name, encoding="utf8")
except:
    fhand = open("mb.txt",encoding="utf8")



counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) +1 # This dictionary has the histogram just not sorted

# Flip to get values on left side to make use of sorted
lst = list()    
for key,val in counts.items():
    newtup = (val,key)
    lst.append(newtup)
#sort it decending
lst = sorted(lst, reverse=True)

#print new list but only top 10

for val,key in lst[:10]:
    print(key,val)

x = counts.get('the')
print(x)