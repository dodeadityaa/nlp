from nltk import FreqDist
from nltk.tokenize import word_tokenize

text = ("Balonku ada lima Rupa-rupa warnanya Hijau, kuning, kelabu Merah muda dan biru Meletus balon hijau DOR! Hatiku sangat kacau Balonku tinggal empat Kupegang erat-erat")
token = word_tokenize(text)
fdist = FreqDist(token)
print(token)
fdist = FreqDist(text)
fdist.most_common()