import re
import random as r

#read The Odyssey
file  = "test.txt"
novel = open(file,"r")
text  = novel.read()

wordArr = [w for w in re.split('\W',text) if w]


word_Graph = {}

for i in range(len(wordArr)-1):
	word      = wordArr[i]
	next_Word = wordArr[i+1]
	if word not in word_Graph:
		word_Graph[word] = {wordArr[i+1]:1.}
	elif word in word_Graph:
		if next_Word not in word_Graph[word]:
			word_Graph[word][next_Word] = 1.
		elif next_Word in word_Graph[word]:
			word_Graph[word][next_Word] += 1.



seed = wordArr[int(r.random()*len(wordArr))]
sentance = seed
word = seed
for i in range(100):
	rand = r.random()
	total = sum(word_Graph[word].values())
	a = 0
	for next_word in word_Graph[word]:
		a+=word_Graph[word][next_word]/total
		if rand<a:
			pword = word
			word = next_word
			break
	sentance+=' '+next_word
# 	print(pword,word_Graph[pword])
print sentance

