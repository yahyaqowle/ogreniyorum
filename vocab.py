report = open('A words.txt', 'w', encoding='utf-8')

with open('change to word.txt', 'r', encoding='utf-8') as f:
    for line in f:
        report.write(line.split(' ')[0])
report.close()