import re
from nltk.stem import PorterStemmer, WordNetLemmatizer

# 1. Extract words with only alphabets
alpha_words = re.findall(r'\b[a-zA-Z]+\b', text_clean)

# 2. Remove stopwords again
filtered_alpha = [w for w in alpha_words if w not in stop_words]

# 3. Stemming
stemmer = PorterStemmer()
stemmed = [stemmer.stem(w) for w in filtered_alpha]

# 4. Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(w) for w in filtered_alpha]

# 5. Compare
print("Stemmed:", stemmed)
print("Lemmatized:", lemmatized)
