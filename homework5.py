# Homework 5: Functions, Lists, Dictionaries, sets and Randomness

import random, math

# Part 1: Count each letter in a string

def count_each_letter(string):
    letter_count = {} 
    countingstring = string.lower().split() 
    for word in countingstring:
        for letter in word:
            if letter.isalpha():  
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1 
    for key, value in sorted(letter_count.items()):
        print(f"{key}: {value}") 



# Part 2: Inventory management




def add_fruit(inventory, fruit, quantity=0):
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity 
    return inventory 



# Part 3: Lottery ticket analysis and simulation

my_tickets = [[7, 17, 37, 19, 23, 43],
              [7, 2, 13, 41, 31, 43],
              [2, 5, 7, 11, 13, 17],
              [13, 17, 37, 19, 23, 43]]


computerscientist = '''Well would you look at that! I have 4 tickets. Can I win the lottery? Maybe? Maybe not.''' # has nothing to do with the code but I thought it was funny to add a quote here.

# Part 3.1
def draw6():
    return [random.randint(1, 50) for _ in range(6)] 

# Part 3.2

def compare_draw_and_ticket(ticket, draw):
    ticket_set = set(ticket) 
    draw_set = set(draw) 
    
    matches = ticket_set.intersection(draw_set) 
    
    return len(matches) 

# Part 3.3

def lotto_matches(tickets, draw):
    return [compare_draw_and_ticket(ticket, draw) for ticket in tickets] 
# Part 3.4


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1): # Basically copied from Assignment 3 teehee (except this time i used the math module!!!)
        if n % i == 0:
            return False
    return True
    
def count_primes(draw):
    return sum(1 for number in draw if is_prime(number)) 
 

# Part 3.5

def missed_primes(tickets):
    missing_primes = []
    all_primes = set() 

    for ticket in tickets:
        for number in ticket: 
            if is_prime(number):
                all_primes.add(number) 

    for primes in range(2, 50):
        if primes not in all_primes and is_prime(primes): 
            missing_primes.append(primes)

    return missing_primes


# Part 3.6



def average_draws(tickets, target):
    total = 0
    for _ in range(20): 
        draws = 0 # 
        while True: 
            draws += 1 
            draw = draw6() 
            matches = lotto_matches(tickets, draw)
            if any(match >= target for match in matches): 
               
                break
        total += draws 
        print("-", end="", flush=True) # Loading bar. Each dash means a trial is finished... flush = true means dashes are printed now. 
    return total // 20 # after 20 trials, compute the average. I'll have it round down to the nearest integer 


# ok... let's give em the test
def main():
    # Part 1 test

    count_each_letter("ThiS is String with Upper and lower case Letters")
    print() # spacing... I'm using empty print functions to separate the tests so it's eaiser to read




    # part 2 test

    # hope these work...
    new_inventory = {} # Empty Dict to test our functions
    add_fruit(new_inventory, "strawberries", 10)
    print("strawberries" in new_inventory) # should return true
    print(new_inventory["strawberries"]== 10) # should return true
    add_fruit(new_inventory, "strawberries", 25)
    print(new_inventory["strawberries"]== 35) # should return true
    print() 
    # good. test passed.
    # So, we add the key "strawberries" with a value of 10. Since it didnt exist in the dict, it was added (to avoid a key error) Now we add 25 to it since it already exists in the dict. The value is now 35.
    # guess i DID learn something from testing in the interpreter.

    # part 3 test


    # part 3.1
    print(draw6()) # nothing special, just making sure the function works.
    print() 
    # part 3.2
    print(compare_draw_and_ticket([42, 4, 7, 11, 1, 13], [2, 5, 7, 11, 13, 17]) == 3) # should return True...
    print() 
    # part 3.3
    print(lotto_matches(my_tickets, [42, 4, 7, 11, 1, 13]) == [1, 2, 3, 1]) # for part 3.6, this would've passed a trial if the target was 3
    print()
    # part 3.4
    print(count_primes([42, 4, 7, 11, 1, 13]) == 3) # should return true...
    print()
    # part 3.5
    print(missed_primes(my_tickets) == [3, 29, 47]) # should return true...
    
    # part 3.6
    
    print("I will now compute the avarages. Each dash you see in the console means a trial is complete.")
    print()
    print("Computing average draws. Target is 3 matches.")
    print("Average draws:", average_draws(my_tickets, 3)) 
    print("Done.")
    print()
    print("Computing average draws. Target is 4 matches.")
    print("Average draws:", average_draws(my_tickets, 4))
    print("Done.")
    print()
    print("Computing average draws. Target is 5 matches. This will take a bit.")
    print("Average draws:", average_draws(my_tickets, 5)) 
    print("Done.")
    print()
    print("All tests complete!")
    # The averages will vary each execution due to randomness!

if __name__ == "__main__":
    main()


  