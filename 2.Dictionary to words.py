report = open('A words VOCAB.txt', 'w', encoding='utf-8')

with open('A words Qaamuus.txt', 'r', encoding='utf-8') as f:
    for line in f:
        report.write(line.split(' ')[0])
report.close()