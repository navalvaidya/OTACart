# -*- coding: utf-8 -*-

'''
	
	In this code sentiment analysis (or opinion mining to be more accurate) is being performed.
	The structure of the text used is as follows:
	->Each text is a list of sentences.
	->Each sentence is a list of tokens.
	->Each token is a tuple of three elements: a word form (the exact word that appeared in the text),
	  a word lemma (a generalized version of the word), and a list of associated tags.
	Input: "review.csv" file generated at runtime when we search for a particular Hotel's details.
	       The contents of the csv file are then converted in the structure mentioned above.
	Output:Number of positive reviews.
	       Number of negative reviws.
	Two dictionaries in the form of yml files are also used to classify a review into postive and negative.
	The yml files used are:positive.yml,negative.yml and inverter.yml 
'''
import csv
import nltk
import yaml
import sys
print ("inside sentiment")
class Splitter(object):
    def __init__(self):
        self.nltk_splitter = nltk.data.load('tokenizers/punkt/english.pickle') 
        '''
        This tokenizer divides a text into a list of sentences,
	by using an unsupervised algorithm to build a model for abbreviation
	words, collocations, and words that start sentences.
        
        '''
        self.nltk_tokenizer = nltk.tokenize.TreebankWordTokenizer()
        '''
       	This tokenizer assumes that the text is presented as one sentence per line,
	where each line is delimited with a newline character.
	The only periods to be treated as separate tokens are those appearing
	at the end of a line.
	It does the following
	- split standard contractions, e.g. ``don't`` -> ``do n't`` and ``they'll`` -> ``they 'll``
	- treat most punctuation characters as separate tokens
	- split off commas and single quotes, when followed by whitespace
	- separate periods that appear at the end of line
	'''

    def split(self, text):
        """
        input format: a paragraph of text
        output format: a list of lists of words.
            e.g.: [['this', 'is', 'a', 'sentence'], ['this', 'is', 'another', 'one']]
        """
        sentences = self.nltk_splitter.tokenize(text)
        tokenized_sentences = [self.nltk_tokenizer.tokenize(sent) for sent in sentences]
        return tokenized_sentences
	

class POSTagger(object):       
    def pos_tag(self, sentences):
        """
        input format: list of lists of words
            e.g.: [['this', 'is', 'a', 'sentence'], ['this', 'is', 'another', 'one']]
        output format: list of lists of tagged tokens. Each tagged tokens has a
        form, a lemma, and a list of tags
            e.g: [[('this', 'this', ['DT']), ('is', 'be', ['VB']), ('a', 'a', ['DT']), ('sentence', 'sentence', ['NN'])],
                    [('this', 'this', ['DT']), ('is', 'be', ['VB']), ('another', 'another', ['DT']), ('one', 'one', ['CARD'])]]
        """

        pos = [nltk.pos_tag(sentence) for sentence in sentences]
        pos = [[(word, word, [postag]) for (word, postag) in sentence] for sentence in pos]
        return pos

class DictionaryTagger(object):
    def __init__(self, dictionary_paths):
        files = [open(path, 'r') for path in dictionary_paths]
        dictionaries = [yaml.load(dict_file) for dict_file in files]
        map(lambda x: x.close(), files)
        self.dictionary = {}
        self.max_key_size = 0
        for curr_dict in dictionaries:
            for key in curr_dict:
                if key in self.dictionary:
                    self.dictionary[key].extend(curr_dict[key])
                else:
                    self.dictionary[key] = curr_dict[key]
                    self.max_key_size = max(self.max_key_size, len(key))

    def tag(self, postagged_sentences):
        return [self.tag_sentence(sentence) for sentence in postagged_sentences]

    def tag_sentence(self, sentence, tag_with_lemmas=False):
        """
        the result is only one tagging of all the possible ones.
        The resulting tagging is determined by these two priority rules:
            - longest matches have higher priority
            - search is made from left to right
        """
        tag_sentence = []
        N = len(sentence)
        if self.max_key_size == 0:
            self.max_key_size = N
        i = 0
        while (i < N):
            j = min(i + self.max_key_size, N) #avoid overflow
            tagged = False
            while (j > i):
                expression_form = ' '.join([word[0] for word in sentence[i:j]]).lower()
                expression_lemma = ' '.join([word[1] for word in sentence[i:j]]).lower()
                if tag_with_lemmas:
                    literal = expression_lemma
                else:
                    literal = expression_form
                if literal in self.dictionary:
                    #self.logger.debug("found: %s" % literal)
                    
                    is_single_token = j - i == 1
                    original_position = i
                    i = j
                    taggings = [tag for tag in self.dictionary[literal]]
                    tagged_expression = (expression_form, expression_lemma, taggings)
                    if is_single_token: #if the tagged literal is a single token, conserve its previous taggings:
                        original_token_tagging = sentence[original_position][2]
                        tagged_expression[2].extend(original_token_tagging)
                    tag_sentence.append(tagged_expression)
                    tagged = True
                else:
                    j = j - 1
            if not tagged:
                tag_sentence.append(sentence[i])
                i += 1
        return tag_sentence


def value_of(sentiment):
    if sentiment == 'positive': 
        return 1
    if sentiment == 'negative':
        return -1
    return 0
def sentence_score(sentence_tokens, previous_token): 
    global pos_cnt,neg_cnt  
    if not sentence_tokens:
        return 
    else:
			
        current_token = sentence_tokens[0]
        tags = current_token[2]
        for tag in tags:
            if value_of(tag)==1:
                pos_cnt=pos_cnt+1
                if previous_token is not None:
                        previous_tags = previous_token[2]
                        if 'inv' in previous_tags:
                            pos_cnt=pos_cnt-1
                            neg_cnt=neg_cnt+1 
                return sentence_score(sentence_tokens[1:], current_token)			
            if value_of(tag)==-1:
                neg_cnt=neg_cnt+1
                if previous_token is not None:
                        previous_tags = previous_token[2]
                        if 'inv' in previous_tags:
                            pos_cnt=pos_cnt+1
                            neg_cnt=neg_cnt-1 
                return sentence_score(sentence_tokens[1:], current_token)
        return sentence_score(sentence_tokens[1:], current_token)

def sentiment_score(review):
    for sentence in review:
        sentence_score(sentence, None)












#the program begins from here


pos_cnt=0
neg_cnt=0
csvfile = open('%s/review_data.csv'%sys.argv[1],'rt',encoding="utf-8")  			#open the csv file to read reviews
csvFileArray = []      					#to store the entire csv file row by row                 
for row in csv.reader(csvfile):	
    csvFileArray.append(row)
text=""
for i in range (0,len(csvFileArray)):			
    for item in csvFileArray[i]:
        ans=item.replace('“','')  		#to remove unicode characters from string
        item=ans.replace('”','')
        text=text+' '+item			#text stores the entire csv file contents to be processed
splitter = Splitter()
splitted_sentences=splitter.split(text) 		#call to split function
print ("4")
postagger = POSTagger()					
pos_tagged_sentences = postagger.pos_tag(splitted_sentences) #call to pos_tag function with splitted sentences as parameter
dicttagger = DictionaryTagger([ '%s/positive.yml'%sys.argv[1], '%s/negative.yml'%sys.argv[1],'%s/inverter.yml'%sys.argv[1]])
dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)
sentiment_score(dict_tagged_sentences)
if pos_cnt+neg_cnt > 100:
    pos_cnt=100-neg_cnt
#Final Output
print ("priinting argv[2]")
print (sys.argv[2])
outputfile=open(sys.argv[2],'w')
pos_output=str(pos_cnt)+"\n"
neg_output=str(neg_cnt)+"\n"
outputfile.write(pos_output)
outputfile.write(neg_output)
outputfile.close()




	
