# Homework 2: Variables, Expressions, and Statements

# Part 1

day = int(input("Enter a day number: "))
if day == 0:
    print("Sunday")
elif day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
else:
    print("Invalid input") 

# Part 2

start_day = int(input("What day of the week did you stay: "))
stay = int(input("How many days: "))
return_day = (start_day + stay) % 7
if return_day == 0:
    print("Sunday")
elif return_day == 1:
    print("Monday")
elif return_day == 2:
    print("Tuesday")
elif return_day == 3:
    print("Wednesday")
elif return_day == 4:
    print("Thursday")
elif return_day == 5:
    print("Friday")
elif return_day == 6:
    print("Saturday")
else:
    print("Invalid input") 

# Part 3

# Opposites:
# 1. a > b: a < b
# 2. a >= b: a < b
# 3. a >= 18 and day ==3: a < 18 or day != 3
# 4. a >= 18 and day !=3: a < 18 or day == 3


# Part 4

# Outcomes:
# 3 == 3: True
# 3 != 3: False
# 3 >= 4: False
# not (3 < 4): False

# Part 5 

# Going up to down from the truth table in the assignment instructions:
# False
# True
# True
# True
# False
# True
# False
# True

# Part 6

score = float(input("Enter your score: "))
if score >= 75:
    print("First")
elif score <= 74 and score >= 70:
    print("Upper second")
elif score <= 69 and score >= 60:
    print("Second")
elif score <= 59 and score >= 50:
    print("Third")
elif score <= 49 and score >= 45:
    print("F1 Supp")
elif score <= 44 and score >= 40:
    print("F2")
else:
    print("F3") # This has got the be the strangest grading system i've seen

# Part 7

a = 2.0 ** 0.5 # Isn't this square root of 2?
print(a, a*a)
print(a*a == 2.0) # Returns False?? I see. This is because of the precision of floating point numbers. 

# Part 8



a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

epsilon = 0.000001  

if (abs(a**2 + b**2 - c**2) < epsilon or
    abs(a**2 + c**2 - b**2) < epsilon or
    abs(b**2 + c**2 - a**2) < epsilon): 
    print("True")
else:
    print("False")