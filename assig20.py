import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string 

#nltk.download('punkt')
#nltk.download('stopwords')

# Sample text
text = "OMG!!! This is not a good time to talk 😂"

tokens=word_tokenize(text)

stop_words=set(stopwords.words('english'))

cleaned=[ 
         word.lower()
         for word in tokens
         if word.lower() not in stop_words and word not in string .punctuation]

cleaned_text=" ".join(cleaned)

print("original text:")

print(text)

print("\nCleaned Text:")
print(cleaned_text)