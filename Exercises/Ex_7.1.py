fname = input('Enter filename:')
try:
    fhandle = open(fname)
except:
    print('File name cant be opened. Check file extension')
    quit()

for line in fhandle:
    line = line.rstrip()
    print(line.upper())