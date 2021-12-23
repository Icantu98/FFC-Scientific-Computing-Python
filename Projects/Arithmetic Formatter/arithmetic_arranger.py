import unittest
import re


### THIS IS WHAT IM WORKING ON FOR PROBLEM
def arithmetic_arranger(problems, math=None):
  arranged_problems = ''
    # Length Error check
  if len(problems) > 5: # WORKS
      arranged_problems = 'Error: Too many problems.'
      return arranged_problems
    
    # Format is x + y = z
  x = []
  y = []
  x_length = []
  y_length = []
  real_length = []
  if math == True: 
    z = []

  for item in problems:
      parts = item.split() 
        #ERROR CHECKS
      if not parts[0].isnumeric() or not parts[2].isnumeric(): # WORKS
          arranged_problems = 'Error: Numbers must only contain digits.'
          return arranged_problems
      if parts[1] != '+' and parts[1] != '-': # WORKS
          arranged_problems = "Error: Operator must be '+' or '-'."
          return arranged_problems
      if len(parts[0]) > 4 or len(parts[2]) > 4: # WORKS
          arranged_problems = "Error: Numbers cannot be more than four digits."
          return arranged_problems
        
        # MATH LOGIC
      if math is True: # Do math if Math = True
          answer = 0
          if parts[1] == '+':
              answer = int(parts[0]) + int(parts[2])
          elif parts[1] == '-':
              answer = int(parts[0]) - int(parts[2])
          else:
              arranged_problems = "Error: Operator must be '+' or '-'."
              return arranged_problems
          parts.append(str(answer))
      x.append(parts[0])          # Stores X value
      y.append((parts[1], parts[2])) # Stores the operation sign and Y value
      if math == True:
          z.append(parts[3]) # if Math = True 4th number is the answer

    ### String management
  for item in x:
      x_length.append(len(item))
  for item in y:
      y_length.append(len(item[1]))
  for count in range(0,len(x_length)):
      if x_length[count] >= y_length[count]:
          real_length.append(x_length[count])
      else:
          real_length.append(y_length[count])
      real_length_int = (int(real_length[count])) + 2
      real_length[count] = real_length_int


    ### Build output
    # X values
  i = 0
  for x_string in x_length: 
      spcLen = real_length[i] - x_string
      spc = ''
      for spcCount in range(1,spcLen+1):
          spc = spc + ' '
      arranged_problems = arranged_problems + spc
      arranged_problems = arranged_problems + x[i]
      arranged_problems = arranged_problems + "    "
      i = i + 1
  arranged_problems = arranged_problems.rstrip()
  arranged_problems = arranged_problems + '\n'

    # Y values
  i = 0
  for y_string in y_length: 
      arranged_problems = arranged_problems + y[i][0] + " "
      spcLen = (real_length[i] - 2) - y_string
      if spcLen > 0:
          spc = ""
          for spcCount in range(1, spcLen+1):
              spc = spc + " "
          arranged_problems = arranged_problems + spc
      arranged_problems = arranged_problems + y[i][1]
      arranged_problems = arranged_problems + "    "
      i = i +1
  arranged_problems = arranged_problems.rstrip()
  arranged_problems = arranged_problems + '\n'

    # Dashes
  for dashLen in real_length:
      for dashCount in range (1, dashLen+1):
          arranged_problems = arranged_problems + '-'
      arranged_problems = arranged_problems + "    "
  arranged_problems = arranged_problems.rstrip()
  if math == True:
    arranged_problems = arranged_problems + '\n'
  else:
    return arranged_problems
    # Z values
  if math == True:
      i = 0
      for prob in z:
          spcLen = real_length[i] - len(prob)
          for spcCount in range (1, spcLen+1):
              arranged_problems = arranged_problems + " "
          arranged_problems = arranged_problems + prob
          arranged_problems = arranged_problems + "    "
          i = i + 1
      arranged_problems = arranged_problems.rstrip()
  return arranged_problems

#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))```
### END OF FUNCTION
#arithmetic_arranger(Data,True)
#print(arithmetic_arranger(Data))
#test = '''
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))
#'''
print('made it to end')