# filepath = "testaddcoma.txt"
#
# with open(filepath, encoding='utf-8') as f:
#     lines = f.read().splitlines()
#
# with open(filepath, 'w', encoding='utf-8') as f:
#     for line in lines:
#         f.write(line + "\n")

filepath = "testaddcoma.txt"

with open(filepath, encoding='utf-8') as f:
    lines = f.read().splitlines()

with open(filepath, 'w', encoding='utf-8') as f:
    for line in lines:
        f.write(line + "\n")



