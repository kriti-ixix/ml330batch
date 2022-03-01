# Importing the libraries
import json
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.sequence import pad_sequences
import colorama
from colorama import Fore, Style, Back
import random
import pickle


# Loading the files
colorama.init()
with open('intents.json') as intents:
    data = json.load(intents)

model = keras.models.load_model('chat_model')

with open('tokenizer.pkl', 'rb') as token:
    tokenizer = pickle.load(token)

with open('label encoder.pkl', 'rb') as encoder:
    label_encoder = pickle.load(encoder)


# Initialising
max_length = 20
print(Fore.YELLOW + "Start talking to the bot and enter quit to exit" + Style.RESET_ALL)


# Main loop
while True:
    print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end = "")
    inp = input()

    if inp.lower() == 'quit':
        break

    result = model.predict(pad_sequences(tokenizer.texts_to_sequences([inp]),
    truncating="post", maxlen=max_length))    

    tag = label_encoder.inverse_transform([np.argmax(result)])

    for i in data['intents']:
        if i['tag'] == tag:
            print(Fore.GREEN + "Bot: " + Style.RESET_ALL, np.random.choice(i['responses']))