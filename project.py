import json
import string
import random

import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
""" import tensorflow as tf
from tf.keras import Sequential
from tf.keras.layers import Dense, Dropout """
nltk.download("punkt")
nltk.download("wordnet")

data_file = open("intents.json",)
data = json.load(data_file)

print(data)

words = []
classes = []
data_X = []
data_y = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tokens = nltk.word_tokenize(pattern)
        words.extend(tokens)
        data_X.append(pattern)
        data_y.append(intent["tag"]) ,

    if intent["tag"] not in classes:
        classes.append(intent["tag"])

lemmatizer = WordNetLemmatizer()

words = [lemmatizer.lemmatize(word.lower()) for words in words if word not in string.punctation]
words = sorted(set(words))
classes = sorted(set(classes))