#!/usr/bin/python

if __name__ == '__main__':
    # a = []
    # for i in range(5):
    #     a.append(input())
    # for key in a:
    #     print(key)
    a = input()
    a, b = a.split()
    c = int(b) / int(a)
    c = c * 100   
    c = round(c, 3)
    t = str(c).split('.')
    if len(t[1]) == 2:
        c= t[0] + '.' + t[1] + '0'
    elif len(t[1]) == 1:
        c= t[0] + '.' + t[1] + '00'
    else:
        c = str(c)
    print(c + '%')