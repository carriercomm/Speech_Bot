import re #for regular expressions
import random 

import numpy as np

file       = "texts/Jane_Austen.txt"
text       = open(file,"r").read()


word_Array = re.findall(r"[\w']+|[.,!?;]", text)

#for testing perposes this will keep the same randomness
random.seed(203)
desired_Sentance_Length = 10 #desired length of the sentance


#function to chose a random weighted index
def weighted_choice(weights):
    totals = []
    running_total = 0

    for w in weights:
        running_total += w
        totals.append(running_total)

    rnd = random.random() * running_total
    for i, total in enumerate(totals):
        if rnd < total:
            return i

#generate the original word graph
word_Graph = {}
for i in range(len(word_Array)-1):
	word      = word_Array[i]
	next_Word = word_Array[i+1]
	if word not in word_Graph:
		word_Graph[word] = {word_Array[i+1]:1.}
	elif word in word_Graph:
		if next_Word not in word_Graph[word]:
			word_Graph[word][next_Word] = 1.
		elif next_Word in word_Graph[word]:
			word_Graph[word][next_Word] += 1.
word_Graph_original = word_Graph

#includes word history in calcuating temporary new weights
def getNewWeights(graph,word_Array,sentance_Array,desired_Sentance_Length,n=1):
	ratio = (len(sentance_Array)/abs(.1+desired_Sentance_Length-3.))**22
	if len(sentance_Array)<n:
		n=len(sentance_Array)
	for j in range(2,n+1):
		for i in range(len(word_Array)-j):
			next_Word = word_Array[i+j]
			word = word_Array[i+j-1]
			if (next_Word == '.'):
				graph[word][next_Word] += ratio
			if word_Array[i:i+j]==sentance_Array[-j:]:
				graph[word][next_Word] += j**3*100
	return(graph)


seed     = 'a'
sentance_Array = [seed]
word     = seed

while (sentance_Array[-1] not in ['.','!','?']) or (any(title in sentance_Array[-5:-1] for title in  ['dr' , 'Mr' , 'mrs' , 'ms' , 'miss'])):
	# word_Graph = getNewWeights(word_Graph,word_Array,sentance_Array,desired_Sentance_Length)
	weights    = word_Graph[word].values()
	w_index    = weighted_choice(weights)
	next_word  = word_Graph[word].keys()[w_index]
	word       = next_word
	sentance_Array.append(next_word)

def create_String(sentance_Array):
	"Creates a string from an array of words"
	sentance = ' '.join(sentance_Array).lower().capitalize()

	#if there is an extra space before punctuation this removes it
	punctuation = [',',';','.','?','!']
	for mark in punctuation:
		sentance = sentance.replace(' '+mark,mark)
	return(sentance)

sentance = create_String(sentance_Array)
print sentance