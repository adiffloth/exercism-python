import re
from collections import Counter


def count_words(sentence):
    sentence = re.sub('[^a-z0-9\' \n\t]+', ' ', str.lower(sentence))
    words = [w.strip('\'') for w in sentence.split()]
    return dict(Counter(words))
