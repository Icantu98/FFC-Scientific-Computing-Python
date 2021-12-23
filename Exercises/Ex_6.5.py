str_var = 'X-DSPAM-Confidence: 0.8475'
colpos = str_var.find(':') # where in the string is the colon

piece = str_var[colpos+1:]
value = float(piece.strip())
print(value)