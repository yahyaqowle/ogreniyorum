import codecs
import codecs
report = open('cleaned somali dictionary/Y words Qaamuus.csv', 'w', encoding='utf-8')
f = open("somali dictionary/Y words Qaamuus.txt", "r", encoding='utf-8')

a = f.read().split()
report.write(str(a))
report.close()




