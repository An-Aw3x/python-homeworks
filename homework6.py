# Homework 6: Files, Dictionaries, and Sets
import random

# Part 1: Opening a file and reading it

def us_capitals():
    state_capitals = {}
    with open("US_States-1.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            stripping = line.strip() # removes whitespacing in each line
            if stripping: 
                parts = line.strip().split('\t') # some states have 2 words in 'em. we can split by tab then remove whitespacing again
                if len(parts) == 2: 
                    state, capital = parts[0], parts[1] # The first index is the state, the second is the capital
                    state_capitals[state] = capital
    return state_capitals 

# Part 1.1: Capitals quiz

def capitals_quiz(state_capitals):
    states = list(state_capitals.keys())
    random.shuffle(states) # so the order is random
    correct_answers = 0
    incorrect_answers = 0  
    print("Welcome to US capitalz Quiz. Any time, type 'exit' to quit.")
    for state in states:
        answer = input(f"What is the capital of {state}? ").strip().lower() # removing whitespace and lowering the case to avoid issues
        if answer.lower() == "exit":
            print("Ok cya")
            break
        elif answer.lower() == state_capitals[state].lower():
            print("Yes!! that's correct!")
            correct_answers += 1
        else:
            print(f"Oh no! That's incorrect. The correct answer is {state_capitals[state]}.")
            incorrect_answers += 1
    percent = (correct_answers / len(states)) * 100 # decided to add a percentage score!
    print(f"That's all folks! You got {correct_answers} correct and {incorrect_answers} incorrect answers.")
    print(f"Your score is {percent:.2f}%")

# Part 2: Encrypting a file

# we'll use 2 functions



code = {"A": "@", "B": "8", "C": "(", "D": "+", "E": "3", "F": "#", "G": "6", "H": "4", "I": "1", "J": ",",
        "K": "<", "L": "7", "M": "0", "N": "^", "O": "9", "P": "%", "Q": "/", "R": "2", "S": "$", "T": "-", 
        "U": "*", "V": "&", "W": ">", "X": "{", "Y": "[", "Z": "]", "a": "}", "b": ":", "c": ";", "d": "=",
        "e": "?", "f": "!", "g": "~", "h": "`", "i": "|", "j": "_", "k": "'", "l": "\"", "m": ".", "n": ",",
        "o": "<", "p": ">", "q": "?", "r": "@", "s": "#", "t": "$", "u": "%", "v": "^", "w": "&", "x": "*",
        "y": "(", "z": ")"}

def encryptfile(filetoread, filetoencrypt):
    with open(filetoread, "r") as f:
        lines = f.readlines() 
    
    with open(filetoencrypt, "w") as f:
        for line in lines:
            for letter, encrypting in code.items(): # try reading this line of code out loud, it sounds like "beginning encryption process..."" :)
                line = line.replace(letter, encrypting) 
            f.write(line)


def displayfile(openfile):
    with open(openfile, "r") as f:
        encryption = f.read()
        print(encryption) # this will display the encrypted file
    
# Part 3: Counting words in a sentence, from a file

def words_per_sentence(openfile):
    sentence_and_words = {}
    with open(openfile, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripping = line.strip()
            if stripping:
                words = stripping.split()
                sentence_and_words[stripping] = len(words)
    for key, value in sentence_and_words.items():
        print(f"{key}: {value} words") # this is kinda similar to Assignment 5. But instead of counter letters, we're counting words

# Part 4: Unique words in a file

def unique_words(openfile):
    with open(openfile, "r") as f:
        lines = f.readlines()
        unique_words = set()
        for line in lines: # outer loop to read each line
            stripping = line.strip() # Removes whitespace, yes empty things are counted
            if stripping: # ONLY read the lines that actually have something in them (i mean you COULD remove this but the function would process faster)
                words = stripping.split() 
                for word in words:
                    unique_words.add(word.lower()) # for case sensitivity
    return unique_words





# Part 5: Finding the largest word in a file
def largest_word(openfile):
    largest_word = "" # to avoid a name error
    with open(openfile, "r") as f:
        poem = f.read()
        words = poem.split()
        for word in words:
            if word.isalpha() and len(word) > len(largest_word): # replaces the largest word if the current word is longer than the largest word
                largest_word = word
    return largest_word


def main():

    # Part 1
    state_capitals = us_capitals()
    print(state_capitals) # this is just to see if the function works.
    print() # spacing
    # part 1.1
    capitals_quiz(state_capitals)
    print()
    # part 2

    encryptfile("RomeoJuliet-1-1.txt", "encrypted.txt")
    displayfile("encrypted.txt")
    print()
    # part 3

    words_per_sentence("RomeoJuliet-1-1.txt")
    print()
    # part 4

    unique_words_list = unique_words("RomeoJuliet-1-1.txt")
    for word in unique_words_list:
        print(word)
    print()

    # part 5

    largest_word_in_file = largest_word("RomeoJuliet-1-1.txt")
    print(f"The largest word in the file is: {largest_word_in_file}")


if __name__ == "__main__":
    main()
