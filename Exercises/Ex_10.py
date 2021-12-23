name = input('Enter file name: ')
try:
    fhand = open(name)
except:
    fhand = open("clown.txt")

di = dict()
for lin in fhand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0)+1

#print(di)

x = sorted(di.items())
#print(x[:5])

# Flips 
temp = list()
for k,v in x:
    newt = (v,k)
    temp.append(newt)

temp = sorted(temp, reverse=True)

# Print them out nicely
for v,k in temp[:5]:
    print(k,v)



