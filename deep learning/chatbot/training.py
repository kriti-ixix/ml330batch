# Importing the Libraries
import json
import numpy as np
from tensorboard import summary
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
import pickle


# Data Preparation
with open("intents.json", 'r') as file:
    data = json.load(file)

training_sentences = [] # Possible user inputs
training_labels = [] # Corresponding tags
labels = [] # Unique tags
responses = [] # Lists of responses

for intent in data["intents"]:
    for patterns in intent["patterns"]:
        training_sentences.append(patterns)
        training_labels.append(intent["tag"])
    responses.append(intent['responses'])

    if intent['tag'] not in labels:
        labels.append(intent['tag'])


num_classes = len(labels)


# Label Encoding
lblEncoder = LabelEncoder()
lblEncoder.fit(training_labels)
training_labels = lblEncoder.transform(training_labels)


# Tokenization
vocab_size = 1000
emdedding_dim = 16
max_length = 20
oovToken = "<OOV>"

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oovToken)
tokenizer.fit_on_texts(training_sentences)
word_index = tokenizer.word_index
print(word_index)

sequences = tokenizer.texts_to_sequences(training_sentences)
padded_sequences = pad_sequences(sequences, maxlen=max_length)


# Neural Network
model = Sequential()
model.add(Embedding(vocab_size, emdedding_dim, input_length=max_length))
model.add(GlobalAveragePooling1D())
model.add(Dense(16, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

history = model.fit(padded_sequences, np.array(training_labels), epochs=500)


# Saving the model

model.save('chat_model')

with open('tokenizer.pkl', 'wb') as token:
    pickle.dump(tokenizer, token)

with open('label encoder.pkl', 'wb') as encoder:
    pickle.dump(lblEncoder, encoder)