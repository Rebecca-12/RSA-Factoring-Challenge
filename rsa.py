#!/usr/bin/env python3


import math

def rsa_factorize_number(number):
    i = 2
    while i <= math.sqrt(number):
        if number % i:
            i += 1
        else:
            return f"{number}={i}*{number//i}"

    return f"{number}={number}*1"  # If the number is prime

def main(filename):
    with open(filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            result = rsa_factorize_number(number)
            print(result)

if __name__ == "__main__":
    main("tests/rsa-1") 
