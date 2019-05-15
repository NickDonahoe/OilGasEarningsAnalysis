import pandas as pd
import re
import string
import unicodedata

import contractions

from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = stopwords.words('english')
stop_words.extend(['said', 'would', 'subject', 'use', 'also', 'like'])
stop_words = set(stop_words)


### NOTE!!!!!
### This code is structured this way for demonstration purposes and could be heavily optimized

def tokenize_text(text):
    """Deconstruct contractions and return tokenized list of words"""
    text = contractions.fix(text)
    words = word_tokenize(text)
    return words

def to_lowercase(tokens):
    """Lowercase all words"""
    lower_words = [w.lower().strip() for w in tokens]
    return lower_words

def remove_punctuation(tokens):
    """Remove punctuation from list of tokenized words"""
    table = str.maketrans('', '', string.punctuation)
    clean_tokens = [w.translate(table) for w in tokens]
    return clean_tokens

def remove_stopwords(tokens, min_word_len):
    """Remove stopwords and short words from list of tokenized words"""
    valued_tokens = []
    for w in tokens:
        if w not in stop_words and len(w)>=min_word_len:
            valued_tokens.append(w)
    return valued_tokens

def remove_non_ascii(tokens):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in tokens:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words

def lemmatize_words(tokens):
    """Normalizes variations of tokens through lemmatization using WordNet"""
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in tokens:
        lemma = lemmatizer.lemmatize(word)
        lemmas.append(lemma)
    return lemmas

def clean_text(text, min_word_len=4):
    """Master function to pass text through preprocessing stages"""
    if type(text) is str:
        words = tokenize_text(text)
        words = remove_non_ascii(words)
        words = to_lowercase(words)
        words = remove_punctuation(words)
        words = remove_stopwords(words, min_word_len)
        words = lemmatize_words(words)
        return words