import spacy
from nltk.tokenize import word_tokenize


nlp = spacy.load("en_core_web_sm")


#function to remove stopwords
def remove_stopwords(text):
    
    stopwords = nlp.Defaults.stop_words
    tokenize = word_tokenize(text)
    text_without_sw = [word for word in tokenize if word not in stopwords]
    return text_without_sw


# Tokenizing word using Spacy 
def word_tokenize(text): 
    
    doc = nlp(text)
    words = [token.text for token in doc]
    return words 

# Tokenizing sent using Spacy 
def sent_tokenize(text):
    
    doc = nlp(text)
    sent = [token.sent for token in doc]
    return sent

# removing punctuation using Spacy
def remove_puncutation(text):
    
    doc = nlp(text)
    punct = [word for word in doc if word.is_punct== False]
    return punct

# Converting to lower case
def to_lower(text):
    
    lower = text.lower()
    return lower 

# applying lemmatization
def lemmatization(text):
    
    doc = nlp(text)
    
    token_lemma =  [token.lemma_ for token in doc]
    
    return token_lemma


a = lemmatization("I was running being chased by a dog")
print(a)







    
    
    
