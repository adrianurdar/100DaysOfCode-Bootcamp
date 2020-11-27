import pandas

alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")

# Ask user input
user_input = input("Enter a word: ").upper()
user_input_list = [letter for letter in user_input]

# 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# {letter, code}
phonetic_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}

# 2. Create a list of the phonetic code words from a word that the user inputs.
phonetic_list = [phonetic_dict[letter] for letter in user_input_list if letter in phonetic_dict]
print(phonetic_list)
