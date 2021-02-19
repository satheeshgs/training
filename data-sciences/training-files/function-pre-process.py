import re
import nltk
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# the function junk_out() removes everything that is above 'Dear Sir,' and below 'Thanks and Regards'. These phrases
# has to be determined by the user. The list 'starts_with' should contain the phrases like 'Thanks and Regards,
# ' and the list 'ends_with' should contain the phrases like 'Dear Sir,'. Then the text between any element
# from 'starts_with' and any element from 'ends_with' is captured and deleted (which actually contains only
# the addresses, salutations, etc.).

# index_finder() is a helper function that gives the index of the very first word that is found in the e-mail.

def index_finder(string, patterns, pos=0):
    indices = [string.find(pattern, pos) for pattern in patterns] # finds the indices of all the words present in the list
    pos_indices = [i for i in indices if i >=0] # ignores the indices for which words are not found
    if pos_indices:
        return sorted(pos_indices)[0] # if non empty, return the smallest index i.e the first word
    else:
        return None

def junk_out(string, starts_with, ends_with):
    string = string.lower() # convert everything to lower case
    start_index = index_finder(string, starts_with) # find the index of the first word from the list in the string
    while start_index != None: # keep deleting until no more words left
        end_index = index_finder(string, ends_with, start_index+1) # index of beginning salutation like good morning
        rem = string[start_index:end_index] # text to be deleted
        string = string.replace(rem, ' ') # deleting the text
        start_index = index_finder(string, starts_with, start_index+1)
    string = re.sub('<.*?>|\{.*?\}', ' ', string) # removes some remaining html tags
    string = re.sub('(\S+@\S+\.\S+|\w\d{4}"\ssrc=.*?>|http\S+)', ' ', string) # removes web urls
    string = re.sub('_+|-+|\*+', ' ', string) # removes hyphens and underscores
    string = re.sub('\s+', ' ', string).strip() # removes white spaces
    return string

# removes all the stopwords and any word having length less than min_len

def rem_stopwords(text, custom_stopwords, min_len=None):
    if type(text) == str: # only apply the algorithm if the input is string
        word_tokens = word_tokenize(text) # breaking the sentence into tokens
        if min_len != None:
            return ' '.join([w for w in word_tokens if w not in custom_stopwords and len(w) > min_len]).strip()
        else:
            return ' '.join([w for w in word_tokens if w not in custom_stopwords]).strip()
    else:
        return ' '


# For the purpose of model building, only alphabets will be helpful. So, we remove everything else.

def rem_nums(text, lemmatization= True):
    text = re.sub('[a-z]{2}\d+\s', ' ', text) # removes some tokens like za670059
    text = re.sub('[^a-zA-Z]', ' ', text) # removes everything but alphabets
    text = re.sub(' +', ' ', text).strip() # removes white spaces
    if lemmatization == True:
        return ' '.join(WordNetLemmatizer().lemmatize(w) for w in word_tokenize(text) if len(w) > 1) # lemmatisation
    else:
        return ' '.join(w for w in word_tokenize(text) if len(w) > 1)

#vectorizing to convert words to numbers

def vectoriser(text):
    tfidf = TfidfVectorizer(analyzer='word', max_features=2000,lowercase= False,ngram_range = (1,2))
    X = tfidf.fit_transform([text]).toarray()
    return X

#generating predictions
#removing this as this is needed for batch processing.
#def pred(X):
#   X1 = pd.DataFrame(X)
#   X = X1.values
#   return  X

#This is the final function that needs to be accessed by lambda function.

def preprocessing_wrapper(item):

    CustomerRequest = item.get('customerRequest')
    Subject = item.get('subject')
    text = ' '.join([Subject,CustomerRequest])

    starts_with = ['thank you in advance', 'to:', 'with thanks', 'this email has been scanned',
                    'please consider the environment', 'address', '[external', 'sent:', 'many thanks', 'm:', 'kind regards',
                    'thanks and', 'with kind regards', 'best,', 'thank you,', "warm regard's", 'thanks & regards', 'purchase executive',
                    'thanks in advance', 'regds', 'thanks,', 'thanks &', '(this is a system', 'from:', '|', 'thank’s & regard’s',
                    'rgds', 'warm regards', 'best regards', 'finance, control', 'tel:', 'regards', 'assistant']


    ends_with = ['good afternoon', 'hi ', 'hi,', 're:', 'please find', 'team', 'sir', 'good morning', 'good day',
                         'this is to bring to', 'please take',
                  'thank you for', 'with reference to', 'subject', 'to whom it may concern', 'dear', 'hello', 'ok,']

    additional = ['thanks','co','truncated', 'character','please','hi', 'thanks', 'fw','ref','morning','gu','ea','th','rz','imprintuniqueid','li','div','td','tel','find' 'attached','u','good', 'afternoon','thank','ltd','could','email','request','note','find','need','send','advise','da', 'absm','may','date','following','registered', 'office','term','condition']

    custom_stopwords = stopwords.words('english') + ends_with + additional


    output1 = junk_out(text, starts_with, ends_with)
    output2 = rem_stopwords(output1, custom_stopwords, min_len=None)
    output3 = rem_nums(output2, lemmatization= True)
    output4 = vectoriser(output3)


    return output4
