#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    argc = len(argv)
    if argc <= 1:
        print(0)
    else:
        argv[1:] = list(map(int, argv[1:]))
        result = sum(argv[1:])
        print(result)
