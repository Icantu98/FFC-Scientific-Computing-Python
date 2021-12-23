x = int(input('Pick a number: ')) #ned to make number an int cause input is always string
if x == 3:
    print('Correct!')
if x != 3:
    print('Wrong!')
    if x >= 3:
        print('Too high')
    if x<= 3:
        print('Too low')    
