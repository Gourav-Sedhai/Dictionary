import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def dictionary(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        question = input("Is %s the word you want to search for?\nIf yes then press y and n if no:\n " % get_close_matches(word, data.keys())[0])
        question = question.lower()
        if question == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif question == "n":
            return "There is no such word as %s " % word
        else:
            question = input("Please select the key y or n: \n")
            if question == "y":
                return data[get_close_matches(word, data.keys())[0]]
            elif question == "n":
                return "There is no such word as %s " % word
            else:
                return "Sorry, we are unable to get your answer"
    else:
        return "There is no such word as %s " % word

word = input("Enter the word: ")

output = dictionary(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)