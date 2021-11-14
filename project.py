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
print("test")