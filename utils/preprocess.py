import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower() #making text as lowercase
    text = re.sub(r"[^a-zA-Z0-9]", " ", text) #removing special characters and numbers

    words = text.split()

    words = [word for word in words if word not in stop_words] # removing comman stop words like "the", "is" ...

    return " ".join(words)
