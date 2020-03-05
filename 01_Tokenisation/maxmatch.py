#maxmatch for 01a

# maxMatch(sentence, dictionary) returns word sequence w

# if sentence is empty
# 	return empty list
# for i<- length(sentence) downto 1
# 	firstword = first i chars of sentence
# 	remainder = rest of sentence
# 	if inDictionary
import sys, re

# sentence = 'hihowareyou'
# dictionary = ['hi', 'how', 'are', 'you']

def maxMatch(sentence, dictionary):
	length = len(sentence)
	if sentence == '':
		return ''
	for i in range(length, 0, -1):
		firstword = sentence[0:i]
		remainder = sentence[i:length]
		if firstword in dictionary:
			return firstword + ' ' + maxMatch(remainder, dictionary)
		
	firstword = sentence[0]
	remainder = sentence[1:length]
	return firstword + ' ' + maxMatch(remainder, dictionary)
	
#print(maxMatch(sentence, dictionary))
dictionary = open("ja.dict")
dictionary = dictionary.read()

tokenisedSentences = open("tokenisedSentencesJaDict.txt", "w")
sentences = open("asSentences")
#sentences = sentences.read()
for sentence in sentences:
	newLine = maxMatch(sentence, dictionary)
	tokenisedSentences.write(newLine)
	
# it does it like this... would like it to be flat...
# ['hi', ['how', ['are', ['you', []]]]]
# look at sentence, satrting whole thing going down in string size
# until the string matches st in the dictionary

# cat ja_gsd-ud-test.conllu | grep '# text' | cut -f2 -d'='
# to show all japanese sentences
# /Users/brett/LING-L545/UD_Japanese-GSD/ja_gsd-ud-test.conllu

#cat /Users/brett/LING-L545/UD_Japanese-GSD/ja_gsd-ud-test.conllu | grep '# text' | cut -f2 -d'=' > asSentences 