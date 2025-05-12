# Homework 4: Strings, Lists, and Tuples

# Part 1: Modify a string

def q1():
    prefixes = "JKLMNOPQ"
    suffix = "ack"
    theuletter = "u" # very original variable i know
    for letter in prefixes:
        if letter == "O":
            print(letter + theuletter + suffix) 
        elif letter == "Q":
            print(letter + theuletter + suffix)
        else:
            print(letter + suffix) 

# Part 2: Count the number of letters in a string

def count_letters(string, letter):
    return string.count(letter) 

# Part 3: # Count the number of letters in a string, via finding the index of the letter

def count_letters2(string, letter):
    count = 0
    index = string.find(letter)
    while index != -1: 
        count += 1
        index = string.find(letter, index + 1) 
    return count

# Part 4: Count the number of words in a string that contain vowels


mypoem = '''What is a video game? Video games are videos that play games. Ok not really. But they are a form of entertainment and allows
players to play games on a screen. There are many differnet types of video games. Racing, fighting, adventure, rythm, and many more.
Video games go long back since the 1970s! From Pong, to Super Mario Bros, to Fortnite, Minecraft, video games have evolved. In fact, video games
are like the computer science lately. Yes. they have code! Video games are made by developers!! Though they're mostly developed on languages like C++ and C#, Python
allows game development too! A good example is Pygame. It is a module that allows you to create games in the Python programming language. So if I may ask,
Professor, TEACH US PYGAME!! perhaps one day I'd LOVE to become a game developer. This is the First step. Python is FUN (mostly). and VIDEO Games too.
So here are my favorite video games:

Minecraft
Wii Sports
Fortnite
Super Smash Bros
Mario Kart
Super Mario Bros
The Legend of Zelda
Age of Empires
Stardew Valley
Splatoon 1, 2 and 3


And many more I forgot lol
Thank you for listening to my Ted Talk.
'''



def count_vowels(string):
    vowels = "aeiouAEIOU" 
    wordcount = 0
    vowelcount = 0 
    words = string.replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("+", "").replace("#", "").replace("(", "").replace(")", "").split() 
    for word in words:
        wordcount += 1
        for char in word:
            if char in vowels:
                vowelcount += 1 
                break 
    if wordcount > 0:
        percent = (vowelcount / wordcount) * 100
    else:
        percent = 0
    print(f"Your text contain {wordcount} words. Of these, {vowelcount}, or {percent:.2f}%, contains a vowel.")




    
    
# part 5: PRint a multiplication table

def q5():
    print("  ", end="") 
    for i in range(1, 13):
        print(f"{i:4}", end="") 
    print() 

    print("  " + "-" * 48) 

    for i in range(1, 13): 
        print(f"{i:2}:", end="") 
        for j in range(1, 13):
            print(f"{i * j:4}", end="") 
        print() 

# Part 6: Creating a mirror string then adding it to the original string

def mirror(string):
    reversestring = string[::-1]  
    return string + reversestring 

# Part 7: # Remove all instances of a letter from a string

def remove(string, lettertoremove):
    return string.replace(lettertoremove, "") 
 

    
# Part 8: Count the number of times a substring occurs in a string

def count_substrings(string, substring): 
    count = 0
    index = string.find(substring) 
    while index != -1: 
        count += 1
        index = string.find(substring, index + 1)
    return count 


# part 9:  Remove the first instance of a substring from a string

def remove_first_substring(string, substring):
    return string.replace(substring, "", 1)

# part 10 Remove all instances of a substring from a string

def remove_all_substrings(string, substring):
    return string.replace(substring, "") 




''' --------------------------------------------------------------------------------------------'''

def main():
    
    # Alright let's test 'em 
    # Part 1
    q1()
    print() # Spacing. All the empty lines are used to separate the tests

    # Part 2
   
    print(count_letters("banana", "a")) # should return 3
    print() 
    
    # part 3
    
    print(count_letters2("banana", "a")) # should return 3 literally does the same thing as part 2
    print() 
    # part 4
    
    count_vowels(mypoem) # Hope you enjoyed my poem. It's amazing, I know.
    print() 

    # part 5
    q5()
    print() 
    # part 6
   
    print(mirror("good") == "gooddoog") # All should return True
    print(mirror("Python") == "PythonnohtyP") 
    print(mirror("") == "") # 
    print(mirror("a") == "aa") 
    print() 
   
    # part 7
    
    print(remove("aplle", "a") == "plle") # All should return True
    print(remove("banana", "a") == "bnn") 
    print(remove("bannana", "z") == "bannana") 
    print(remove("Misissippi", "i") == "Mssspp") 
    print(remove("", "b") == "")
    print(remove("c", "b") == "c") 
    print()

    # part 8
    
    print(count_substrings("Mississippi", "is" ) == 2) # All these should return True
    print(count_substrings("banana", "an") == 2) 
    print(count_substrings("banana", "ana") == 2) 
    print(count_substrings("banana", "nana") == 1) 
    print(count_substrings("banana", "nanan") == 0) 
    print(count_substrings("aaaaaa", "aaa") == 4) # this sucker is the reason why i couldnt use the count function...
    print() 

    # Part 9
    print(remove_first_substring("banana", "an") == "bana") # All should return True
    print(remove_first_substring("bicycle", "cyc") == "bile") 
    print(remove_first_substring("Mississippi", "iss") == "Missippi") 
    print(remove_first_substring("bicycle", "eggs") == "bicycle") 
    print()

    # part 10

    print(remove_all_substrings("banana", "an") == "ba") # All should return True
    print(remove_all_substrings("bicycle", "cyc") == "bile")
    print(remove_all_substrings("Mississippi", "iss") == "Mippi")
    print(remove_all_substrings("bicycle", "eggs") == "bicycle")

    print("Done!")


if __name__ == "__main__":
    main()