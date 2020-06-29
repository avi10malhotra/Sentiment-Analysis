import nltk
import os

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        # declaration of a set in positive-words.txt
        self.positives = set()
        
        # open file for reading
        file = open(positives, "r")
        
        # skip over values starting with ';' using .startswith
        for line in file:
            if line.startswith(';') == False:
                self.positives.add(line.rstrip("\n"))
        file.close()
        
        # declaration of a set in negative-words.txt
        self.negatives = set()
        
        # open file for reading
        file = open(negatives, "r")
        
        # skip over values starting with ';'
        for line in file:
            if line.startswith(';') == False:
                self.negatives.add(line.rstrip("\n"))
        file.close()


    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        # split a tweet into a list of words i.e. tokens
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        
        # set intial score to 0
        score = 0
        
        # change in sum as per classification of the word
        for word in tokens:
            if word.lower() in self.positives:
                score = score + 1
                
            elif word.lower() in self.negatives:
                score = score - 1
            
            else:
                continue
        
        # return the final sum as output and exit cleanly
        return score 
        return 0
