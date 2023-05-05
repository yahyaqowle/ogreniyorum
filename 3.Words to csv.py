report = open('Cleaned Somali words/Somali-Words.csv', 'w', encoding='utf-8')
f = open("Somali Words/Somali-Words.txt", "r", encoding='utf-8')

convert = f.read().split()
report.write(str(convert))
report.close()
