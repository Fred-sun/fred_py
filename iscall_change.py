#!/usr/bin/python

if __name__ == '__main__':
    while True:
        a = int(input("Pleae input a number:"))
        if isinstance(a, int):
            print(a)
            break
    print(a)

    print(bin(a))