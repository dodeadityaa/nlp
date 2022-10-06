from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

factory = StopWordRemoverFactory()

more_stopword = open('stop.txt','r')
data = factory.get_stop_words() + more_stopword

stopword = factory.create_stop_word_remover()
# Kalimat
kalimat = 'dengan menggunakan python dan library sastrawi saya dapat melakukan proses stopword removal'
stop = stopword.remove(kalimat)
print(stop)