#!/usr/bin/python3

for num in reversed(range(97, 123)):
    print("{:c}".format(num if num % 2 == 0 else (num - 32)), end="")
