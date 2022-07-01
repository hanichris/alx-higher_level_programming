#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argc = len(sys.argv)
    if argc <= 1:
        print("0 arguments.")
    elif argc == 2:
        print(f"{argc - 1} argument:")
        print(f"1: {sys.argv[1]}")
    else:
        print(f"{argc - 1} arguments:")
        for index, argument in enumerate(sys.argv[1:], 1):
            print(f"{index}: {argument}")
