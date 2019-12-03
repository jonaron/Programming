import fileinput

def valid_phrase(line):
	dict = {}
	phrase = line.split(" ")
	for word in phrase:
		sortword = ''.join(sorted(word))
		#print(sortword)
		if sortword in dict:
			#print(phrase, " is not valid")
			return False
		else:
			dict[sortword] = 1
	#print(phrase, " is valid")
	return True

count = 0
for line in fileinput.input():
	#if line[-1] == "\n":
		#line = line[:-1]
	if valid_phrase(line[:-1]):
		count += 1
print(count)
