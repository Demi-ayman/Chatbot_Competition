import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize (sentence):
    return nltk.word_tokenize(sentence)


def stem(words):
    return stemmer.stem(words.lower())


def bag_of_words(tokenized_sentence , all_words):
    sentence_words = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx , w in enumerate(all_words):
        if w in sentence_words:
            bag[idx] = 1.0
    return bag 

sentence = ["hello", "how", "are", "you"]
words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
bag = bag_of_words(sentence,words)
#print(bag)

