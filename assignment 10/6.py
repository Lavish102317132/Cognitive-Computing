from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense
import numpy as np

para = "AI is changing the world. Machine learning powers applications. Natural language understanding is growing rapidly."

# 1. Tokenize
tokenizer = Tokenizer()
tokenizer.fit_on_texts([para])
seqs = tokenizer.texts_to_sequences([para])[0]

# 2. Generate training sequences
input_seqs = []
for i in range(1, len(seqs)):
    input_seqs.append(seqs[:i+1])

input_seqs = pad_sequences(input_seqs, padding='pre')

# 3. LSTM model
X = input_seqs[:, :-1]
y = input_seqs[:, -1]
y = np.array(y)

model = Sequential([
    Embedding(len(tokenizer.word_index)+1, 10, input_length=X.shape[1]),
    LSTM(50),
    Dense(len(tokenizer.word_index)+1, activation='softmax')
])
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')
model.fit(X, y, epochs=200, verbose=0)

# Text generation
seed = "ai"
next_words = 3

for _ in range(next_words):
    token_list = tokenizer.texts_to_sequences([seed])[0]
    token_list = pad_sequences([token_list], maxlen=X.shape[1], padding='pre')
    predicted = np.argmax(model.predict(token_list, verbose=0), axis=-1)[0]
    output_word = ''
    for word, index in tokenizer.word_index.items():
        if index == predicted:
            output_word = word
            break
    seed += " " + output_word

print("Generated text:", seed)
