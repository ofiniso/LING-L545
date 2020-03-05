import sys, re

abbr = ['etc.', 'e.g.', 'i.e.', 'c.', 'f.',
				'en.', 'B.C.', 'sq.']

def tokenise(line, abbr):
	line = re.sub(r'([\(\)"?:!;])', r' \g<1> ', line) # g means group
	line = re.sub(r'([^0-9]),', r'\g<1> ,', line) 
	line = re.sub(r',([^0-9])', r', \g<1>', line) 
	line = re.sub(r'  +', ' ', line[:-1]) # collapse sequences of spaces

	output = []
	for token in line.split(' '):
		if token == '':
			continue
		if token[-1] == '.' and token not in abbr: 
			token = token[:-1] + ' .'
		output.append(token)
		
	return ' '.join(output)
	
line = sys.stdin.readline() 
while line != '':
	print(tokenise(line.strip('\n'), abbr)) 
	line = sys.stdin.readline()

