import numpy as np
# import re
# import numpy.core.defchararray as df
import cPickle as pkl



#the first time you run make sure to have w2_.txt downloaded (see readme)
# and uncomment all these line up to pkl.dump
#this will generate a  file that can be read in by cPickle.
#you can then comment them out to save.... only half a second. 


# file = "w2_.txt"
# text = open(file,"r").read()
# word_Array = text.split('\r\n')
# t = np.array([segments.split() for segments in word_Array][:-1])
# pkl.dump( t, open( "save.p", "wb" ) )

t = pkl.load( open( "save.p", "rb" ) )
print('Done with import and preprocessing\n')
print('======================================\n\n')

seed = 'she'
word = seed
sentance = [word]
def weighted_Choice(weights,vals):
	weights = weights.astype(int)
	cs  = np.cumsum(weights) #An array of the weights, cumulatively summed.
	
	idx = np.sum(cs < np.random.rand()*np.max(weights)) #Find the index of the first weight over a random value.
	# print idx
	return vals[idx]



for i in range(10):
	# print seed
	l       = np.where(t[:,1] == word)[0]
	weights = t[l[0]:l[-1]+1,0]
	vals    = t[l[0]:l[-1]+1,2]
	word    = weighted_Choice(weights,vals)
	sentance.append(word)

def create_String(sentance_Array):
	"Creates a string from an array of words"
	sentance = ' '.join(sentance_Array).lower().capitalize()+'.'

	#if there is an extra space before punctuation this removes it
	punctuation = [',',';','.','?','!']
	for mark in punctuation:
		sentance = sentance.replace(' '+mark,mark)
	return(sentance)

print create_String(sentance)

#http://www.ngrams.info/download_coca.asp