import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter: row.code for index, row in data.iterrows()}


def generate_phonetics():
    word = input("enter the word: ").upper()
    try:
        new_list = [nato[letter] for letter in word ]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetics()
    else:
        print(new_list)


generate_phonetics()
