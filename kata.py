import re
from nltk.tag import CRFTagger
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize



frequency = {}
document_text = input("Masukan Kata :")
text_string = document_text.lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:

    print("Frekwensi :",words, frequency[words])

ct = CRFTagger()
ct.set_model_file('all_indo_man_tag_corpus_model.crf.tagger')
hasil = ct.tag_sents([[document_text]])

print("Tagger :",hasil)

factory = StopWordRemoverFactory()

more_stopword = ['dengan', 'saya']
data = factory.get_stop_words() + more_stopword

stopword = factory.create_stop_word_remover()
# Kalimat
stop = stopword.remove(document_text)
print("StopWord :",stop)

sentences = sent_tokenize("text")
sentenceValue = dict()

for sentence in sentences:
    for wordValue in frequency:
        if wordValue[0] in sentence.lower():
            if sentence[:12] in sentenceValue:
                sentenceValue[sentence[:12]] += wordValue[1]
            else:
                sentenceValue[sentence[:12]] = wordValue[1]

sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

# Average value of a sentence from original text
average = int(sumValues/ len(sentenceValue))

summary = ''
for sentence in sentences:
        if sentence[:12] in sentenceValue and sentenceValue[sentence[:12]] > (1.5 * average):
            summary +=  " " + sentence