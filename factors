#!/usr/bin/env python3


import math

def factorize_number(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return f"{number}={i}*{number//i}"
    return f"{number}=1*{number}"  # If the number is prime

def main(filename):
    with open(filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            result = factorize_number(number)
            print(result)

if __name__ == "__main__":
    main("tests/test00")  
