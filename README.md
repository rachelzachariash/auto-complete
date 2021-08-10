# auto-complete
The project is to implementation the autocomplete feature of google

Implementing the feature by having a big data of sentence that could be that the 
user is looking for, the goal is: 
that when the user insert a word (and press enter) the program will give him 5 sentence (with the highest score) 
that the word contains in the sentence.
The score is set by the amount of letter that in place  in the sentence and if their deviations
the score goes down.
To implement the feature their 2 stemps:
1. Offline to create a suffix trie with all the sentence in the data and in each node put at 
most 5 sentence that contain the words that the user insert  
1. When the user insert a word looking in the suffix trie which sentence contain the 
word if the less the 5 sentence try to look for sentence that contain the word with deviations.
