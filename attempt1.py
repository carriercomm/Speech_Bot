import re
import random as r

#for testing perposes this will keep the same randomness
r.seed(12132)
#read The Odyssey
file  = "odysey.txt"
novel = open(file,"r")
text  = novel.read()

wordArr = [w for w in re.split('\W',text) if w]

def weighted_choice(weights):
    totals = []
    running_total = 0

    for w in weights:
        running_total += w
        totals.append(running_total)

    rnd = r.random() * running_total
    for i, total in enumerate(totals):
        if rnd < total:
            return i


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
word_Graph_original = word_Graph

def getNewWeights(graph,wordArr,sentance,n=5):
	if len(sentance)<n:
		n=len(sentance)
	for j in range(2,n+1):
		for i in range(len(wordArr)-j):
			if wordArr[i:i+j]==sentance[-j:]:
				next_Word = wordArr[i+j]
				graph[wordArr[i+j-1]][next_Word] += j
	return(graph)

seed     = wordArr[int(r.random()*len(wordArr))]
sentance = [seed]
word     = seed
for i in range(10):
	word_Graph = getNewWeights(word_Graph,wordArr,sentance)
	weights    = word_Graph[word].values()
	w_index    = weighted_choice(weights)
	next_word  = word_Graph[word].keys()[w_index]
	word       = next_word
	sentance.append(next_word)
	word_Graph = word_Graph_original

print sentance

