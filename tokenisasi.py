from nltk import word_tokenize
import re

frequency = {}
r_string = input("masukan kata :")
tokens = word_tokenize(r_string)
words = [word for word in tokens if re.findall("\w(?:[-\w]*\w)?", word)]
words = [w.lower() for w in words]
for word in words:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = sorted(frequency, key=frequency.get, reverse=True)

for words in frequency_list:
    print(words + " " + str(frequency[words]) + "\n")