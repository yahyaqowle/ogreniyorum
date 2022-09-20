report = open('E words VOCAB.csv', 'w', encoding='utf-8')
f = open("E words VOCAB.txt", "r", encoding='utf-8')

convert = f.read().split()
report.write(str(convert))
report.close()
