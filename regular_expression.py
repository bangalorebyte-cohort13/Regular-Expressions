import re 

# string matching without regular expressions
text = open("melville-moby_dick.txt")
for line in text:
	#strip() removes characters from the beggining and end of string 	
	line = line.strip() 
	word = 'lexicon'
	position = line.find(word)
	#print(position)
	#if position >= 0:
		#print(line)



for line_re in text:
	line_re = line_re.strip()
	#search() finds only the first occurrence of the pattern within the string.
	#if re.search('lexicon',line_re):
		#print(line_re)
		
	
# find line that starts with lexicon
for line in text:
	line = line.strip()
	#if re.search('^The{2,}',line):
		#print(line)

word1= "X-Sieve: CMU Sieve 2.3"
word2 = "X-DSPAM-Result: Innocent"
word3 = "X-Plane is behing schedule: two weeks"


print(re.search('ˆX',word1))


# something that begins with "x-" followed only by 
# upper case and then followed by a colon and then a
# space some more characters
# lets look at a more complicated example

#find any string that matches a string begging with 'X-' followed by no whitespace and one or more characters
# and zero or more characters and then any number between 0 and 9

text1 = "My 2 favorite numbers are 19 and 42"
re = re.findall('[0-9]+',text1)
#print(re)

