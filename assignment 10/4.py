text1 = "AI enables machines to learn from data."
text2 = "Blockchain ensures data security in transactions."

# 1. Preprocessing
tokens1 = set(word_tokenize(text1.lower())) - stop_words
tokens2 = set(word_tokenize(text2.lower())) - stop_words

# a. Jaccard Similarity
jaccard_sim = len(tokens1 & tokens2) / len(tokens1 | tokens2)

# b. Cosine Similarity
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

vec = TfidfVectorizer()
tfidf_cos = vec.fit_transform([text1, text2])
cos_sim = cosine_similarity(tfidf_cos[0:1], tfidf_cos[1:2])[0][0]

print("Jaccard Similarity:", jaccard_sim)
print("Cosine Similarity:", cos_sim)
