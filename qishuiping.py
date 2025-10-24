#!/usr/bin/python3
def deal_count(a):
    if a < 2:
        return 0
    elif a < 3:
        return 1
    else:
        c = a // 3
        d = a % 3
        return  c + deal_count(c+d)
    
if __name__ == '__main__':
    try:
        a = int(input("Please enter a number: "))
    except Exception:
        print("Your number is invalid, Please re-enter a number: ")
        a = int(input())
    res_count = deal_count(a)
    print(res_count)