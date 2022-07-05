#!/usr/bin/python3
import time
import sys
import os


# Function for special printing effects
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
    print()

# Function for clearing the screen


def clear_screen():
    os.system('cls || clear')

# Function for small delay


def fprint(str):
    print("\n" + str)
    time.sleep(0)


def sprint(str):
    print(str)
    time.sleep(0.5)
