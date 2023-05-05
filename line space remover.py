# filepath = "A words Qaamuus.txt"
#
# with open(filepath, 'w', encoding='utf-8') as f:
#     for line in filepath:
#         if not line.isspace():
#             filepath.write(line)



with open("Somali Words/Somali-Dictionary.txt","r", encoding='utf-8') as f, open("Cleaned Somali words/Somali-Dictionary.txt","w", encoding='utf-8') as outfile:
    for i in f.readlines():
        if not i.strip():
            continue
        if i:
            outfile.write(i)