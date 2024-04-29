student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)
alphabetcsv = pandas.read_csv("nato_phonetic_alphabet.csv")
# for(index,row) in alphabetcsv.iterrows():


# alphabetdict = pandas.DataFrame.to_dict(alphabetcsv)

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

dict_alph = {row.letter: row.code for (index, row) in alphabetcsv.iterrows()}
# print(dict_alph)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a Word: ").upper()
list_nato = [dict_alph[letter] for letter in word]
print(list_nato)