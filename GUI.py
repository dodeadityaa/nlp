import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QFileDialog
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk import word_tokenize
import re
import math
from textblob import TextBlob as tb


class GUII (QtWidgets.QMainWindow) :
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super (GUII,self).__init__()
        uic.loadUi("GUII.ui",self)
        self.setWindowTitle("Natural Language Proccesing")
        pybutton = QPushButton('Frekuensi', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(131, 41)
        pybutton.move(10, 660)

        pabutton = QPushButton('Stopword', self)
        pabutton.clicked.connect(self.clickMethodd)
        pabutton.resize(131, 41)
        pabutton.move(350, 660)

        pubutton = QPushButton('Stemming', self)
        pubutton.clicked.connect(self.clickMethoddd)
        pubutton.resize(131, 41)
        pubutton.move(700, 660)

        pobutton = QPushButton('Open', self)
        pobutton.clicked.connect(self.open)
        pobutton.resize(131, 41)
        pobutton.move(870, 210)

        pibutton = QPushButton('summarization', self)
        pibutton.clicked.connect(self.summarizationn)
        pibutton.resize(131, 41)
        pibutton.move(1030, 660)

    def open(self):
        filename = QFileDialog.getOpenFileName(self, "Open File")
        if filename[0]:
            file = open(filename[0], "r")

            with file:
                text = file.read()
                self.lineEdit.setText(text)

    def clickMethod(self):
        frequency = {}
        r_string = self.lineEdit.text()
        tokens = word_tokenize(r_string)
        words = [word for word in tokens if re.findall("\w(?:[-\w]*\w)?", word)]
        words = [w.lower() for w in words]
        for word in words:
            count = frequency.get(word, 0)
            frequency[word] = count + 1

        frequency_list = sorted(frequency, key=frequency.get, reverse=True)

        for words in frequency_list:
            print(words + " " + str(frequency[words]))
            self.Frekuensi_2.setText(words + str(frequency[words]))

    def clickMethodd(self) :
        factory = StopWordRemoverFactory()

        more_stopword = [open("stoplist.txt","r")]
        data = factory.get_stop_words() + more_stopword

        stopword = factory.create_stop_word_remover()
        # Kalimat
        stop = stopword.remove(self.lineEdit.text())
        print("StopWord :", stop)
        self.Stopword_2.setText("StopWord :"+ stop)


    def clickMethoddd(self):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()

        kalimat = self.lineEdit.text()
        katadasar = stemmer.stem(kalimat)
        print(katadasar)
        self.Steamming.setText("Steeming :" + katadasar)

    def summarizationn (self):
        def tf(word, blob):
            return blob.words.count(word) / len(blob.words)

        def n_containing(word, bloblist):
            return sum(1 for blob in bloblist if word in blob)

        def idf(word, bloblist):
            return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

        def tfidf(word, blob, bloblist):
            return tf(word, blob) * idf(word, bloblist)

        document1 = tb(self.lineEdit.text())

        bloblist = [document1]
        for i, blob in enumerate(bloblist):
            print("Top words in document {}".format(i + 1))
            scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
            sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
            for word, score in sorted_words[:3]:
                self.summarization.setText("Word: {}, TF-IDF: {}".format(word, round(score, 5)))
                print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GUII()
    ex.show()
    sys.exit(app.exec_())