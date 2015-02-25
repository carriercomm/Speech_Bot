# Speach_Bot
an attempt at creating a python program to imitate human speach 

<h2>The Original Idea for the Algorithm</h2>
Read in textual data.
create a graph where each node is a word and there are directed edges from that word to any word which has comes after it in any of the textual data. Start with a seed word. To generate the next word read in the current chain of words. Assign weights to the edges to the next words based on how many time the word preceded the next word. When calculating weights also include more heavily weighted those words which came after the same n length chain, with longer n corresponding to higher weighting. With some max n chosen. Statistically chose which edge to follow based on the edge weights.