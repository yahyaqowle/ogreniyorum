# Define the list of abbreviations
abbreviations = ['a', 'ac', 'baay.', 'bot.', 'bul.', 'c.af', 'c.beer', 'c.cimi', 'c.fal', 'c.naf', 'c.nafl', 'ca',
                 'daaw.', 'dd', 'dh', 'dhaq', 'dhm', 'dii.', 'diid', 'dk', 'e', 'eb', 'e.d', 'etno.', 'f', 'fals.',
                 'fiis.', 'fk', 'g', 'h', 'isrog', 'j', 'jool.', 'juqr.', 'ke', 'kh', 'kiim.', 'l', 'ld', 'lg', 'lh',
                 'ly', 'm', 'maan.', 'mg', 'mi', 'mu', 'muus.', 'nax', 'q', 'qaan', 'qf', 'qr', 'riw', 's', 'sh.r',
                 'siyaa.', 'so', 't', 'taar.', 'tegno.', 'to.', 'ti', 'tus', 'u', 'u-j', 'w', 'we', 'wr', 'xi', 'xis']

# Read in the file
with open("unorganized_data.txt", "r") as f:
    lines = f.readlines()

# Initialize variables
current_word = None
current_abbreviation = None
current_meaning = None
current_pair = None
word_meaning_pairs = []

# Loop through each line
for line in lines:
    # Clean up the line by removing leading/trailing white space and converting to lower case
    line = line.strip().lower()

    # If the line starts with 'k', it's a new word
    if line.startswith('t'):
        # Check if there was a current pair and add it to the list of word-meaning pairs
        if current_pair is not None:
            word_meaning_pairs.append(current_pair)

        # Split the line into word and abbreviation
        parts = line.split()
        current_word = parts[0]
        if len(parts) >= 2:
            current_abbreviation = parts[1]
        current_meaning = ' '.join(parts[2:])
        current_pair = {"word": current_word + ' ' + current_abbreviation, "meaning": current_meaning}

    # If the line does not start with 'k', it's a continuation of the meaning of the current word
    else:
        # Check if the line ends with a full stop or comma (which may not indicate the end of the meaning)
        if line.endswith('.') or line.endswith(','):
            current_meaning += ' ' + line
        else:
            # Check if the line contains an abbreviation (which may indicate the end of the meaning)
            parts = line.split()
            if len(parts) > 1 and parts[0] in abbreviations:
                current_meaning += ' ' + line
            else:
                # The current line is part of the current meaning, add it to the current meaning
                current_meaning += ' ' + line

# After looping through all lines, check if the current pair exists and add it to the list of word-meaning pairs
if current_pair is not None:
    word_meaning_pairs.append(current_pair)

# Combine consecutive word-meaning pairs with the same word
combined_pairs = []
for i, pair in enumerate(word_meaning_pairs):
     if i > 0 and pair["word"] == word_meaning_pairs[i - 1]["word"]:
         # Combine the meanings of consecutive word-meaning pairs with the same word
         combined_pairs[-1]["meaning"] += ' ' + pair["meaning"]
     else:
         combined_pairs.append(pair)

# Write the cleaned data to a file
with open("nadiif.txt", "a") as f:
    for pair in combined_pairs:
        f.write(pair["word"] + ": " + pair["meaning"] + "\n")
