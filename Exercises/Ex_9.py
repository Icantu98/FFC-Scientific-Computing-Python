fname = input('Enter File: ')
if len(fname) < 1:
    fname = 'clown.txt' #assumes if left blank will default to clown file
hand = open(fname)

di = dict()

for line in hand:
    lin = line.strip() # gets rid of white space
    #print(lin)
    wds = lin.split() # splits words appart
    #print(wds)
    for w in wds:
        #:ALPHA: Better way of BETA
        # IDIOM: retrieve/create/update counter
        di[w] = di.get(w,0) + 1
        #print(w,di[w])


        # better way of THETA
        #BETA:if they key is not there the count is zero
        #oldcount = di.get(w,0)
        #print(w,':old count =',oldcount)
        #newcount = oldcount + 1
        #di[w] = newcount
        #print(w,':new =',newcount)
        #BETA

        #THETA
        #print(w)
        #if w in di: #if it exists add 1 to ti
            #di[w] = di[w] + 1
        #else:       #if its a new word asign value to 1
            #di[w] = 1
            #print('**NEW**')
        #print(w,di[w])
        #THETA

#print(di)

#now find the most common word
largest = -1
theword = None
for k,v in di.items(): #k = key, v = value
    #print(k,v)
    if v > largest:
        largest = v
        theword = k # capture the key thats the largest 
print('The word "',theword,'" happens ',largest,'times')


