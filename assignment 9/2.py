from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer
nltk.download('wordnet')

ps = PorterStemmer()
ls = LancasterStemmer()
lemmatizer = WordNetLemmatizer()

porter_stemmed = [ps.stem(w) for w in filtered_words]
lancaster_stemmed = [ls.stem(w) for w in filtered_words]
lemmatized = [lemmatizer.lemmatize(w) for w in filtered_words]

print("Porter:", porter_stemmed)
print("Lancaster:", lancaster_stemmed)
print("Lemmatized:", lemmatized)
