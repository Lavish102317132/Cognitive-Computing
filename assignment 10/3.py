from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

docs = [
    "AI is transforming the healthcare industry.",
    "Blockchain provides secure transactions.",
    "Natural Language Processing improves chatbot interactions."
]

# 1. Bag of Words
vectorizer = CountVectorizer()
bow = vectorizer.fit_transform(docs)
print("BOW Feature Names:", vectorizer.get_feature_names_out())

# 2. TF-IDF
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(docs)

# 3. Top 3 keywords
for i, doc in enumerate(docs):
    tfidf_scores = zip(tfidf.get_feature_names_out(), tfidf_matrix[i].toarray()[0])
    sorted_scores = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)[:3]
    print(f"Doc {i+1} Top 3:", sorted_scores)
