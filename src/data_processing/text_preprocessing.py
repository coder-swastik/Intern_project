import re
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer



def preprocess(text):
    """
    Preprocesses the given text by:
    1. Converting to lowercase
    2. Removing punctuation
    3. Removing numbers
    4. Tokenizing text
    5. Removing stopwords
    6. Stemming words
    """
    
    # Convert text to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words]
    
    # Stemming (reducing words to their root form)
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    
    # Reconstruct sentence
    processed_text = " ".join(tokens)
    
    return processed_text
