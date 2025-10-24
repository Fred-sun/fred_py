#!/usr/bin/python
import random

if __name__ == '__main__':
    a = [random.randint(0,500) for i in range(50)]

    print(list(set(a)))
    a = list(set(a))
    print(sorted(a))
    print(len(a))
    print(len(set(a)))