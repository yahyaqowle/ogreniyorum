# filepath = "A words Qaamuus.txt"
#
# with open(filepath, 'w', encoding='utf-8') as f:
#     for line in filepath:
#         if not line.isspace():
#             filepath.write(line)



with open("A words Qaamuus.txt","r", encoding='utf-8') as f, open("A words DB.txt","w", encoding='utf-8') as outfile:
    for i in f.readlines():
        if not i.strip():
            continue
        if i:
            outfile.write(i)