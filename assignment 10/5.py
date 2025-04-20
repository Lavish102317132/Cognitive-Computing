from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

reviews = [
    "This product is amazing and works like a charm!",
    "Worst service ever. Totally disappointed.",
    "It’s okay, not the best but does the job."
]

for review in reviews:
    blob = TextBlob(review)
    print(f"'{review}' => Polarity: {blob.sentiment.polarity}, Subjectivity: {blob.sentiment.subjectivity}")

# Wordcloud for positive
positive_reviews = " ".join([r for r in reviews if TextBlob(r).sentiment.polarity > 0])
wordcloud = WordCloud(width=800, height=400).generate(positive_reviews)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
