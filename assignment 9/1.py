import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import string

nltk.download('punkt')
nltk.download('stopwords')

text = "I love working with machine learning models. They help solve real-world problems and make decisions based on data. I enjoy exploring new algorithms and testing their performance."

# Lowercase and remove punctuation
text_clean = text.lower().translate(str.maketrans('', '', string.punctuation))

# Tokenize
words = word_tokenize(text_clean)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [w for w in words if w not in stop_words]

# Frequency Distribution
freq_dist = Counter(filtered_words)
print(freq_dist)
