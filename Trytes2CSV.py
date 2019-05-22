tern=['A','B','C','D','E','F','G','H','I','J','K',        'L',         'M',  'N',        'O','P', 'Q',    'R', 'S','T', 'U',       'V',         'W',    'X',                           'Y', 'Z', '9']
data=['1','2','3','4','5','6','7','8','9','.','Timestamp','Longi/Lati','PPM','Turbidity','0','PH','Error','\n',' ','C','uSiemens','Volatility','Watts','Use ternary alphabet until 9','?', '?', ',']



inputs = input("Paste ternary or data for conversion(checks for','): ") #ask for input and get input
"""
if ',' in (inputs) #look for ternary data
	print 'input looks like data\n'
	outputs = 'Ternary: ' 

	for character in inputs:
		outputs += (tern[data.index(character)])

	print(outputs)

else: # autodetection of data input for translation to ternary
"""

# This is an example of data turnary: 
# XFL99XCLAY9SXCOUNTY9BFEHBAJEG9O9AEGEO
# 
# Which should result in the following ASCII data: 
# FL,CLAY COUNTY,265821.57,0,15750



TextMode = False					#starts in data mode

outputs = 'Translated data: ' 

for character in inputs:



	if character == "X" and TextMode == False:
		TextMode = True
		print('X Found and removed')
									#debug
	elif character == "9" and TextMode == True:
		TextMode = False
		
	elif TextMode == True:
		outputs += (character)
		
	else:											#"9" appears or at the end of the Alphabet data
		outputs += (data[tern.index(character)])	#translate ternary string to data
	

print(outputs)
