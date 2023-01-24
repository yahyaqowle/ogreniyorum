# report = open('B words VOCAB.txt', 'w', encoding='utf-8')
#
# with open('B words Qaamuus.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         report.write(line.split()[0])
# report.close()

# # Open the output file in write mode
# with open('B words VOCAB.txt', 'w', encoding='utf-8') as report:
#   # Open the input file in read mode
#   with open('B words Qaamuus.txt', 'r', encoding='utf-8') as f:
#     # Iterate over the lines in the input file
#     for line in f:
#       # Split the line into a list of words
#       words = line.split()
#       # Extract the first word from the list
#       first_word = words[0]
#       # Write the first word to the output file on a separate line
#       report.write(first_word + '\n')

with open('B words VOCAB.txt', 'w', encoding='utf-8') as report:
  # Open the input file in read mode
  with open('B words Qaamuus.txt', 'r', encoding='utf-8') as f:
    # Iterate over the lines in the input file
    for line in f:
      # Split the line into a list of words
      words = line.split()
      # Check if the list is not empty
      if words:
        # Extract the first word from the list
        first_word = words[0]
        # Write the first word to the output file on a separate line
        report.write(first_word + '\n')

