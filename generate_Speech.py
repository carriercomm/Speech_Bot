from numpy import cumsum,max
from numpy.random import rand,seed
from re import findall#for regular expressions
seed(203)

class word_Graph(dict):
	"""docstring for graph"""
	def __init__(self,word_Array):
		self.generate_Graph(word_Array)
	def add_Edge(self,v1_Name,v2_Name,weight = 1):
		self[v1_Name] = {v2_Name:weight}
	def generate_Graph(self,word_Array):
		for i in xrange(len(word_Array)-1):
			word      = word_Array[i]
			next_Word = word_Array[i+1]
			if word not in self:
				self.add_Edge(word,next_Word)
			else:
				if next_Word not in self[word]:
					self[word][next_Word] = 1.
				else:
					self[word][next_Word]+=1.

#includes word history in calcuating temporary new weights
def getNewWeights(graph,word_Array,sentance_Array,desired_Length,n=5):
	l = len(sentance_Array)
	if l<n:
		n=l
	for j in range(2,n+1):
		match_Indices = [x for x in xrange(len(word_Array)) if word_Array[x:x+j] == sentance_Array[-j:]]
		for match in match_Indices:
			graph[sentance_Array[-1]][word_Array[match+j]] += j**2
			if word_Array[match+j]=='.':
				period_Weight = 100**(l/desired_Length)
				graph[sentance_Array[-1]][word_Array[match+j]] += period_Weight
	return(graph)

def weighted_Choice(d):
    cs  = cumsum(d.values()) #An array of the weights, cumulatively summed.
    idx = sum(cs < rand()*max(d.values())) #Find the index of the first weight over a random value.
    return d.keys()[idx]


file       = "books/Jane_Austen.txt"
text       = open(file,"r").read().replace('_','')
word_Array = findall(r"[\w']+|[.,!?;]", text)



wg = word_Graph(word_Array)

seed = 'she'
sentance_Array = [seed]
word = seed
desired_Length = 10

while (sentance_Array[-1] not in ['.','!','?']) or (any(title in sentance_Array[-5:-1] for title in  ['dr' , 'Mr' , 'mrs' , 'ms' , 'miss'])):
	print word
	wg_mod = dict(wg)
	getNewWeights(wg_mod,word_Array,sentance_Array,desired_Length)
	next_word  = weighted_Choice(wg_mod[word])
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

print create_String(sentance_Array)
