# Homework 3: Functions, Conditionals, and Recursion

# Part 1: Compute and print the first n triangular numbers
def print_triangular_num(n):
    triangular_num = []
    for i in range(1, n + 1):
        triangular_num.append(i * (i + 1) // 2) 
    for num in triangular_num:
        print(num) 


# Part 2: Find if a number is prime
def is_prime(n): 
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0: 
            return False
    return True

# Part 3: Count the number of digits in a number


def num_digits(n):
    if n == 0: 
        return 1
    count = 0
    n = abs(n) 
    while n > 0:
        n //= 10 
        count += 1
    return count


# Part 4: Count the number of even digits in a number



def num_even_digits(n):
    if n == 0: 
        return 1
    count = 0
    n = abs(n)
    while n > 0:
        digit = n % 10  
        if digit % 2 == 0:
            count += 1 
        n //= 10 
        
    return count

def main():
    # Part 1 Test
    
    print_triangular_num(5)  
    
    # part 2 test
    
    print(is_prime(11)) # true
    print(not is_prime(35)) # true
    print(is_prime(19911121)) # true
    
 
    print(is_prime(4))  # false
    
   
    print(is_prime(247)) 

    # part 3 test
    
    print(num_digits(0) == 1)
    print(num_digits(12345) == 5) 
    print(num_digits(-12345) == 5) 

    # part 4 test

    print(num_even_digits(123456) == 3)
    print(num_even_digits(2468) == 4) 
    print(num_even_digits(1357) == 0) 
    print(num_even_digits(0) == 1) 

    # bonus: part 5

    this = ["I", "am", "not", "a", "crook"]
    that = ["I", "am", "not", "a", "crook"]
    print("Test 1: {0}".format(this is that)) # False??? Ok so let's see. Despite the variables having the same values, they are actually different objects in memory! thus returs false.
    this = that
    print("Test 2: {0}".format(this is that)) 





if __name__ == "__main__":
    main()
else:
    print("This line will never be printed")