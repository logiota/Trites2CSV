tern=['A','B','C','D','E','F','G','H','I','J','K',        'L',         'M',  'N',        'O','P', 'Q',    'R', 'S','T', 'U',       'V',         'W',    'X',                           'Y', 'Z', '9']
data=['1','2','3','4','5','6','7','8','9','.','Timestamp','Longi/Lati','PPM','Turbidity','0','PH','Error','\n',' ','C','uSiemens','Volatility','Watts','Use ternary alphabet until 9','?', '?', ',']



inputs = input("Paste ternary or data for conversion(checks for','): ") #ask for input and get input
"""
if ',' in (inputs) #look for ternary 
	print 'input looks like data\n'
	outputs = 'Ternary: ' 

	for character in inputs:
		outputs += (tern[data.index(character)])

	print(outputs)


else: # autodetection of data input for translation to ternary
#This is an example of data turnary:
#XTEXT9SXAS9SXTEXT9SABCDEFJABC
#Which should result in the following ASCII data:
#TEXT AS TEXT 123456,123
"""

outputs = 'Data: ' 

for character in inputs:							#make an exception for charaters following X
	if character == 'X'	:
		for character in inputs:			
			while (character != '9'):			
				outputs += character			#output the original A-Z trytes
													#need of breaking while loop to avoid getting stuck here
			break
	else :
	outputs += (data[tern.index(character)])	#translate ternary string to data

print(outputs)
