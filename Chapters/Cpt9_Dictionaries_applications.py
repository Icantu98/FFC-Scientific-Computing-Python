ccc = {}

ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)

counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for item in names:
    if item not in counts:
        counts[item] = 1
    else:
        counts[item] = counts[item] + 1
print(counts)

# Easy way of loop above
counts = dict()
namess = ['csev','cwen','csev','zqian','cwen']
for name in namess:
    counts[name] = counts.get(name,0) + 1  # .get tells you how many times something inside of dictionary
print(counts)

