text = "Artificial Intelligence (AI) is revolutionizing industries like healthcare and finance. With AI, machines learn from data, improving over time. Natural Language Processing helps computers understand human language. I love studying how algorithms evolve. The future of AI is both exciting and challenging."

# 1. Lowercase and remove punctuation
import string
text_clean = text.lower().translate(str.maketrans('', '', string.punctuation))

# 2. Tokenization
from nltk.tokenize import word_tokenize
tokens_split = text_clean.split()
tokens_word_tokenize = word_tokenize(text_clean)

# 3. Compare split vs word_tokenize
print("Split:", tokens_split)
print("Word_tokenize:", tokens_word_tokenize)

# 4. Remove stopwords
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in tokens_word_tokenize if w not in stop_words]

# 5. Word frequency
from collections import Counter
freq_dist = Counter(filtered_tokens)
print("Word Frequency:", freq_dist)
