import re
import random as r


#read The Odyssey
file  = "texts/PrideAndPrejudice.txt"
file  = "texts/Beowulf.txt"
file = 'texts\HuckFinAndTomSawyer.txt'
# file = 'C:\Users\Jackson\Documents\GitHub\Speech_Bot\emails.txt'
novel = open(file,"r")
text  = novel.read()#.lower()
wordArr = re.findall(r"[\w']+|[.,!?;]", text)
#(?<=dr|mr|mrs|ms|miss).
#need to not asociate periods with these

#for testing perposes this will keep the same randomness
# r.seed(203)
desiredLength = 20 #desired length of the sentance

#function to chose a random weighted index
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

#generate teh original word graph
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

#includes word history in calcuating temporary new weights
def getNewWeights(graph,wordArr,sentance,desiredLength,n=8):
	ratio = (len(sentance)/abs(.1+desiredLength-3.))**22
	if len(sentance)<n:
		n=len(sentance)
	for j in range(2,n+1):
		for i in range(len(wordArr)-j):
			next_Word = wordArr[i+j]
			word = wordArr[i+j-1]
			if (next_Word == '.'):
				graph[word][next_Word] += ratio
			if wordArr[i:i+j]==sentance[-j:]:
				graph[word][next_Word] += j**3*100
	return(graph)

#a seed for the generater to start
seed     = wordArr[int(r.random()*len(wordArr))]
# seed = 'she'
sentance = [seed]
word     = seed

while (sentance[-1] not in ['.','!','?']) or (any(title in sentance[-5:-1] for title in  ['dr' , 'Mr' , 'mrs' , 'ms' , 'miss'])):
	word_Graph = getNewWeights(word_Graph,wordArr,sentance,desiredLength)
	weights    = word_Graph[word].values()
	w_index    = weighted_choice(weights)
	next_word  = word_Graph[word].keys()[w_index]
	word       = next_word
	sentance.append(next_word)
	word_Graph = word_Graph_original


sentance = ' '.join(sentance).lower().capitalize()
s = ''
for i in range(len(sentance)-1):
	if sentance[i+1] in [',',';','.','?','!']:
		s+=sentance[i+1]
	elif sentance[i] not in [',',';','.','?','!']:
		s+=sentance[i]
print s