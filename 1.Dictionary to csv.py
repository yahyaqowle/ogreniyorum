import codecs
import codecs
report = open('E words Qaamuus.csv', 'w', encoding='utf-8')
f = open("E words Qaamuus.txt", "r", encoding='utf-8')

a = f.read().split()
report.write(str(a))
report.close()




