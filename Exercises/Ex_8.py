han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    #print('Line: ',line)
    wds = line.split()
    #print('Words:',wds)

    # Guardian line. Is made stronger with better assumption from <1 to < 3
    if len(wds) < 3: #checks if line has 0 values in it cause wds[0] breaks on empty lines
        #print('skip blank line')
        continue
    if wds[0] != 'From' : #check if first word is From if not conintue
        #print('ignore')
        continue

    print(wds[2]) # prints day

print('***************************')

han = open('mbox-short.txt')
# Gaudian line with and OR statement
for line in han:
    line = line.rstrip()
    wds = line.split()

    # Guardian line. Is made stronger with better assumption from <1 to < 3
    if len(wds) < 3 or wds[0] != 'From':  #Checks IN ORDER of rules listed
        continue
    print(wds[2])
    