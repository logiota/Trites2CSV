tern=['A','B','C','D','E','F','G','H','I','J','K',        'L',         'M',  'N',        'O','P', 'Q',    'R',  'S',   'T', 'U',       'V',         'W',    'X',                           'Y', 'Z', '9']
data=['1','2','3','4','5','6','7','8','9','.','Timestamp','Longi/Lati','PPM','Turbidity','0','PH','Error','\n','Speed','C','uSiemens','Volatility','Watts','Use ternary alphabet until 99','?', '?', ',']



inputs = input("Paste ternary or data for conversion(checks for','): ")
"""
if ',' in (inputs)
	print 'input looks like data\n'
	outputs = 'Ternary: ' 

	for character in inputs:
		outputs += (tern[data.index(character)])

	print(outputs)


else: # autodetection of data input for translation to ternary
#XTEXT9XAS9XTEXT9ABCDEFJABC
"""

outputs = 'Data: ' 

for character in inputs:					
	if character == 'X'	:				#make an exception for charaters following X
		while (character != '9'):
				outputs += character		#instead output the original alphabet
				if 				#need of breaking while loop to avoid getting stuck here
	else :
		outputs += (data[tern.index(character)])	#translate ternary string to data

print(outputs)
