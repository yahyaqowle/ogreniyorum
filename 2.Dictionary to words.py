report = open('test A Words vocab.txt', 'w', encoding='utf-8')

with open('E words Qaamuus.txt', 'r', encoding='utf-8') as f:
    for line in f:
        report.write(line.split(' ')[0])
report.close()