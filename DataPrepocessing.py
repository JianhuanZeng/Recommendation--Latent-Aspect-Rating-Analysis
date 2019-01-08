################# read the key words of each aspect ###########################
import pandas as pd

c_list=[]
with open('hotel_criteria_words.dat', 'r') as txt:
    for critr in txt:
        c_list.append(critr.split())

critr={c_list[i][0]:c_list[i][1:38] for i in range(len(c_list))}
critr.keys()

#critr['<room>'][27]
key=pd.DataFrame(critr)




################################### data reading ##############################
import pandas as pd
import os
import re

# read data
dt = pd.read_csv(os.path.join("/Users/cengjianhuan/Documents/Fall2017/BigDataAnalysics/Project/RawData", 'HotelsReviews.csv'), header=None)

# different funcs
from nltk.corpus import stopwords

def text2wordlist( text):
    # remove non-letters
    txt=re.sub("[^a-zA-Z]"," ",text)
    # convert to lower case
    words=txt.lower().split()
    # remove stop words
    stop_wds=set(stopwords.words("english"))
    stop_wds.add('nan')
    words = [w for w in words if not w in stop_wds]
    return words
#// download engilish stop words for nltk library
#// download the punkt tokenizer for sentence splitting
import nltk.data
nltk.download()

############################## tokenizer ######################################
import nltk.data
tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
"""
the function to clean a text to sentences in wordlist
"""
def text2sentences( text, tokenizer):
    # the NLTK tokenizer to split the paragraph into sentences
    raw_sentences = tokenizer.tokenize(text.strip())
    sentences = []
    for raw_sentence in raw_sentences:
        if len(raw_sentence) > 0:
            sentences += text2wordlist( raw_sentence)
    return sentences

############################## text analysis ######################################

# clean the whole dataset
hotel=dt['Hotel Name'][1]
texts=dt['reviews']
HotelID=[hotel]
all_words_i=[] # the clean texts in a hotel d
D_hotel={} # the clean data set
print('now for hotel: '+str(hotel))
for i in range(len(texts)):
    if dt['Hotel Name'][i]==hotel:
        all_words_i.append(text2sentences(texts[i],tokenizer))
    else:
        print('now for hotel: '+str(hotel)+"    id: "+ )
        HotelID.append(dt['Hotel Name'][i])
        D_hotel[hotel]=all_words_i
        hotel=dt['Hotel Name'][i]
        all_words_i=[]
        all_words_i.append(text2sentences(texts[i],tokenizer))


# to get a vacabulary list (wordsd) of a hotel(d)
def vac_d(txt):
    """
    vac_d(): extract to a list
    input: txt = dict['12 Oaks Motor Hotel'], all clean sentences for hotel"12 Oaks Motor Hotel"
    output: words_d = a vacabulary list: words_d of a hotel:d
    """
    wordsd=[]
    for i in txt:
        wordsd+=i
    return wordsd

# build a word_count dictionary
def words_count(input_d):
    # a raw word count feature for text input_d
    t2={}
    for word in input_d:
        if word in t2.keys():
            t2[word]+=1
        else:
            t2[word]=1
    return t2
