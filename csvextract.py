report = open('A words.csv', 'w', encoding='utf-8')
f = open("change to word.txt", "r", encoding='utf-8')

convert = f.read().split()
report.write(str(convert))
report.close()
