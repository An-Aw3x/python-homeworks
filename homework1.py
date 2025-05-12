# Homework 1: Introduction to Python. The Basics


# Part 1 Put strings in variables and print them
word1 = "All"
word2 = "work"
word3 = "and"
word4 = "no"
word5 = "play"
word6 = "make"
word7 = "Jack"
word8 = "a"
word9 = "dull"
word10 = "boy"
word11 = "who’s"
word12 = "tired." 

print(word1, word2, word3, word4, word5, word6, word7, word8, word9, word10, word11, word12) 

# Part 2: Basic math operations
result = 6 * (1 - 2) 
print(result)

# Part 3 Basic math operations with variables
bruce = 6
print(bruce + 4) 

# Part 4: Calculate compound interest
P = 10000
n = 12
r = 0.08

t = int(input("Enter the number of years the money will be compounded for: "))

A = P * (1 + r/n)**(n*t) # Wait a minute this formula looks familar, I learned that in MAC1105!!

print(f"The final amount after {t} years is: ${A:.2f}") # I hope this is right, I don't know if I did it right



# Part 5: Evaluate numerical expressions

print(5 % 2) # 1
print(9 % 5) # 4
print(15 % 12) # 3
print(12 % 15) # 12
print(6 % 6) # 0
print(0 % 7) # 0
try:
    print(7 % 0) 
except ZeroDivisionError:
    print("You can't divide by zero, that's illegal") 



    # Part 6: Calculate the time the alarm will go off

    current_hour = 14  
    alarm_in_hours = 51

    days = alarm_in_hours // 24
    extra_hours = alarm_in_hours % 24

    alarm_hour = (current_hour + extra_hours) % 24

    print(f"The alarm will go off in {days} days and {extra_hours} hours, at {alarm_hour}:00.") 

  