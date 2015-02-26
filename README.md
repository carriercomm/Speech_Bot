# Speech_Bot
an attempt at creating a python program to imitate human speach 

<h2>The Original Idea for the Algorithm</h2>
Read in textual data.
create a graph where each node is a word and there are directed edges from that word to any word which has comes after it in any of the textual data. Start with a seed word. To generate the next word read in the current chain of words. Assign weights to the edges to the next words based on how many time the word preceded the next word. When calculating weights also include more heavily weighted those words which came after the same n length chain, with longer n corresponding to higher weighting. With some max n chosen. Statistically chose which edge to follow based on the edge weights.

<h3> Things to work on </h3>
<ul>
<li>[x]Take in sentance history for more precise edge weights</li>
<li>[]Consider using <a href = 'http://www.nltk.org/'>the NLTK </a> To check sentance validity</li>
<li>[]Pull text from facebook/gmail (working on it)</li>
<li> []better random weight selection algorithm </li>
<li>[]Create graph class for simpler future work</li>
<li>[]Include external graph library</li>
<li> []Vizualizing word network for debugging/cuz it would be cool</li>
<li>[]Add puntuation(in progress)</li>
<li> []How to include beginings/ends of sentances???</li>
<li> []Add ability to export word graph to JSON for interactive d3 visual</li>
</ul>


<p>gold readings have not desisted From the inevitable place weary of evil to comply either with offers to leader of the loan etc The Scop s handwork I swung as ferocious as ealles and his sorrow that were With weapon Him who complished it The men do it The Project Gutenberg 1 Though high helmet till he at the vapor The horn anon sang the king and Beowulf s son she injured his worth and reported to the weeping and my journey Wild beasts and his hand and beaker battle the daughter named it 40 The Helmingish lady then sadly in</p>
