
import re
import deepcut
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import string as stri
from wordcloud import WordCloud


# =============================================================================
# Custom Dictionary for Pre-Processing
# =============================================================================
wordlist = r'C:\Users\prakarnk\Python\Text Sentiment_V3\0.Dictionary\Custome_Dict.txt'
stopwrd = r'C:\Users\prakarnk\Python\Text Sentiment_V3\0.Dictionary\visit_stopwords.txt'

# =============================================================================
# Text Pre-Processing Function
# =============================================================================

def token(text,custom_dic = None,sep=None):
    """
    Remove WhiteSpace & Word Tokenize.
    
    Parameters
    ----------
    text : string or list of string
        sentence for tokenization
    custom_dict : list of word or arrays, default None
        thai word groupping
    sep : string, default None
        specifies a string to be used as the word separator (space, tab, newline, return, formfeed).

    """
    if type(text) == str:
        new_text = text.split(sep=sep)
    else:
        new_text = text.str.split(pat=sep)   
    tokenize = []
    for i in range(len(new_text)):
        x = deepcut.tokenize(new_text[i],custom_dict=custom_dic)
        tokenize = tokenize + x
    return [item for item in tokenize if item != ' ']


def sub_url(text):
    """
    Substitute URL to "WebUrl".
    
    """
    url = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','WebUrl ', text) 
    return url

# substitute FWD Max
def sub_fwdmax(text): 
    """
    Group all word that relevant to fwd MAX application.
    
    """
    fwd = re.sub('fwd max','fwdmax', text) 
    return fwd

# Remove Symbol
def remove_symbol(text):
    """
    Remove special characters, tabs and new lines.
    
    """
    remove_text = text.translate(str.maketrans('', '', stri.punctuation))
    return remove_text

# Remove StopWord
def remove_stopword(text,stopword_lst):
    
    """
    Remove commonly used words (such as “the”, “a”, “an”, “in”) 
    
    Parameters
    ----------
    text : list of word
        word token in list , e.g. ['Hello','World].
    stopword_lst : list of word or arrays, default None
        custom list of stop words.
    
    Example
    ----------
    >>> remove_stopword(['hello','to','the','world'],stopword_lst=['to','the'])
        Before: ['hello','to','the','world']
        After: ['hello','world']
    """
    if stopword_lst == None:
        pass
    else:
        add_stopset = []
        f = open(stopword_lst,'r')
        for line in f:
            add_stopset.append(line.strip())    
        th_stop = [i for i in add_stopset]
        tokens = [i for i in text if not i in th_stop]
    #     tokens = text.replace(word, mylist2[mylist1.index(word)])
    return tokens

def join_token(text):
    return ' '.join(text)


def remove_pol(text):
    """
    Convert a policy number into "policynumber".
    
    """   
    lst_sub = []
    old_string = text.strip().lower()
    for substr in old_string.split():
        url = re.sub('([a-z])[0-9]{8}','policynumber', substr) 
        lst_sub.append(url)
    new_string = ' '.join(lst_sub).strip()
    new_string = re.sub('\s\s+', ' ', new_string).strip()
    return new_string

def remove_dspace(text):
    """
    Remove double space from a sentence.
    
    """   
    new_string = re.sub('\s+', ' ', text.strip().lower()).strip()
    return new_string

def processTHChar(string):
    """
    Correct repetitive Thai alphabets in sentence.

    Example
    ----------
    >>> Before: ''ประกันนนนภัยยยยย''
        After: 'ประกันภัย'
    >>> Before: 'ประกันนนน'
        After: 'ประกัน'
    """   
    mystr = string.strip()
    mystr = re.sub(r'(?<=[เ])([ดมยอ])\1{2,}$', r'\1\1', mystr)
    mystr = re.sub(r'(?<=[เ])(?![ดมยอ])([ก-ฮ])\1{1,}$', r'\1', mystr)
    mystr = re.sub(r'(?<=[แ])([ดนบปพมวส])\1{2,}$', r'\1\1', mystr)
    mystr = re.sub(r'(?<=[แ])(?![ดนบปพมวส])([ก-ฮ])\1{1,}$', r'\1', mystr)
    mystr = re.sub(r'(?<=[โ])([ดน])\1{2,}$', r'\1', mystr)
    mystr = re.sub(r'(?<=[โ])(?![ดน])([ก-ฮ])\1{1,}$', r'\1', mystr)
    mystr = re.sub(r'(?<=[ไ])([ก-ฮ])\1{1,}$', r'\1', mystr)
    mystr = re.sub(r'(?<=[ใ])([ก-ฮ])\1{1,}$', r'\1', mystr)
    mystr = re.sub(r'(?<=[ใ])([ก-ฮ])\1{1,}$', r'\1', mystr)
    mystr = re.sub(r'(?<=[ะ])([งบ])\1{2,}$', r'\1\1', mystr)
    mystr = re.sub(r'(?<=[ะ])(?![งบ])([ก-ฮ])\1{1,}$', '', mystr)
    mystr = re.sub(r'(?<=[า])([ง])\1{2,}$', r'\1\1', mystr)
    mystr = re.sub(r'(?<=[า])(?![ง])([ก-ฮ])\1{1,}$', r'\1', mystr)
    mystr = re.sub(r'(?<=[า])([ขฃฅฆฌผฝหอฮ])\1{0,}$', '', mystr)
    mystr = re.sub(r'(?<=[ิ])([ก-ฮ])\1{1,}$', r'\1', mystr)
    mystr = re.sub(r'(?<=[ิ])([ขฃฅฆฌถผฝภหอฮ])\1{0,}$', '', mystr)
    mystr = re.sub(r'(?<=[ี])([ง])\1{2,}$', r'\1\1', mystr)
    mystr = re.sub(r'(?<=[ี])(?![ง])([ก-ฮ])\1{1,}$', r'\1', mystr)
    mystr = re.sub(r'(?<=[ี])([ขฃฅฆฌถผฝภวศษหฬอฮ])\1{0,}$', '', mystr)
    mystr = re.sub(r'(?<=[ึ])([ก-ฮ])\1{1,}$', r'\1', mystr)
    mystr = re.sub(r'(?<=[ึ])(?![กงดนบม])([ก-ฮ])\1{0,}$', '', mystr)
    mystr = re.sub(r'(?<=[ือ])([ง])\1{2,}$', r'\1\1', mystr)
    mystr = re.sub(r'(?<=[ือ])(?![ง])([ก-ฮ])\1{1,}$', r'\1', mystr)
    mystr = re.sub(r'(?<=[ุ])([ง])\1{2,}$', r'\1\1', mystr)
    mystr = re.sub(r'(?<=[ุ])(?![ง])([ก-ฮ])\1{1,}$', r'\1', mystr)
    mystr = re.sub(r'(?<=[ุ])(?![ง])([ฃฅฆผฝหอฮ])\1{0,}$', '', mystr)
    mystr = re.sub(r'(?<=[ู])([ง])\1{2,}$', r'\1\1', mystr)
    mystr = re.sub(r'(?<=[ู])(?![ง])([ก-ฮ])\1{1,}$', r'\1', mystr)
    mystr = re.sub(r'(?<=[ู])(?![ง])([ฃฅฆผฝภหฬอฮ])\1{0,}$', '', mystr)
    mystr = re.sub(r'(?<=[ำ])([น])\1{2,}$', r'\1\1', mystr)
    mystr = re.sub(r'(?<=[ำ])(?![น])([ก-ฮ])\1{1,}$', '', mystr)
    mystr = re.sub(r'(?<=[ั])([ก-ฮ])\1{1,}$', r'\1', mystr)
    mystr = re.sub(r'(?<=[์])([ก-ฮ])\1{0,}$', '', mystr)    
    mystr = re.sub(r'(?![ง])([ก-ฮ])\1{2,}', r'\1', mystr)
    return mystr

# =============================================================================
# Pre-Processing
# =============================================================================

def preprocess_sentence(sentence: str,stopwrd,wordlist,sep='|'):
    
    # Lower Case
    result = sentence.lower()
                               
    # Fix PolicyNo
    result = remove_pol(result)
    
    # Fix Url
    result = sub_url(result)
    
    # Fix FWD Max
    result = sub_fwdmax(result)
    
    # Remove Symbol
    result = remove_symbol(result)
     
    # Remove Double space
    result = remove_dspace(result)
    
    # Remove Normalisation
    result = processTHChar(result)  
    
    # Tokenize
    result = token(result,wordlist,sep='|')
    
    # Stopword
    result = remove_stopword(result,stopwrd)
    
    return result

def preprocess_df(DataFrame,stopwrd,wordlist,sep='|'):
   
    # Lower Case
    new_DataFrame = DataFrame.apply(lambda x: x.lower())
                               
    # Fix PolicyNo
    new_DataFrame = new_DataFrame.apply(lambda x: remove_pol(x))
    
    # Fix Url
    new_DataFrame = new_DataFrame.apply(lambda x: sub_url(x))
    
    # Fix FWD Max
    new_DataFrame = new_DataFrame.apply(lambda x: sub_fwdmax(x))
    
    # Remove Symbol
    new_DataFrame = new_DataFrame.apply(lambda x: remove_symbol(x))
    
    
    # Remove Double space
    new_DataFrame = new_DataFrame.apply(lambda x: remove_dspace(x))
    
    # Tokenize
    new_DataFrame = new_DataFrame.apply(lambda x: token(x,wordlist,sep='|'))

    # Stopword
    new_DataFrame = new_DataFrame.apply(lambda x: remove_stopword(x,stopwrd))
    
    return new_DataFrame

    
def display_wordcloud( title, n_components, max_components_per_row=1):
    word_power = pd.read_pickle("word_power.pickle")
    word_power['VAR_NAME'] = word_power['VAR_NAME'].str.replace('_visit', '')
    word_power = word_power[(word_power['GINI']>0)]
    word_power = word_power.drop(columns=['PREDICTIVE_POWER'])
    word_power = dict(zip(word_power['VAR_NAME'].tolist(), word_power['GINI'].tolist()))

    # settings
    h, w = 500,900       # height, width of each image  
    figsize = [15, 15]   # figure size, inches
    if n_components < max_components_per_row:
        ncols = int(n_components)
        nrows = int(np.ceil(n_components/ncols))
    else:
        ncols = int(max_components_per_row)
        nrows = int(np.ceil(n_components/ncols))
             
    # create figure (fig), and array of axes (ax)       
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
#     ax = np.array(ax)
    fig.subplots_adjust(top=0.8)
    item = 0
    for i, axi in enumerate(ax.flat):
        axi.imshow(WordCloud(font_path='C:\\Windows\\Fonts\\Angsana New\\angsana.ttc',
                             width=w,
                             height=h,
                             max_words=50*(item+1),
                             max_font_size=100,
                             relative_scaling=0.5,
                             colormap='Dark2',
                             regexp=r"[\u0E00-\u0E7Fa-zA-Z']+",
                             normalize_plurals=True).generate_from_frequencies(word_power))
        rowid = i // ncols
        colid = i % ncols
        axi.set_title(title+str(item+1)) 
        axi.axis('off')
        item+=1      
    plt.tight_layout(True)
    plt.show()     

def bigram(text,n=2):
    """
    Group consecutive n tokens into one token.
    
    Parameters
    ----------
    text : list of word
        word token in list , e.g. ['Hello','World].
    n : integer, default 2
        number of tokens that we would like to group
    
    Example
    ----------
    >>> ngram(['hello','to','the','world'],n=2)
        Before: ['hello','to','the','world']
        After: ['hello to','to the','the world']
    """  
    n_gram = list()
    
    for token in zip(text[:-1],text[1:]):
        
        n_gram.append(' '.join(token))
    
    
    return n_gram
