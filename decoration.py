def foo(func):
    def wraper(*args,**kwargs):
        print("This wraper start:")
        func(*args,**kwargs)
        print('This is wraper end:')
    return wraper

@foo
def show01():
    print("The funciton is show----001")
    print('*'*30)

@foo
def show02(name,age):
#    print(f"My name is {name}, age is {age}")
    print('*'*30)
@foo
def show03(name,age=18):
    print(f"The funciotn is show -----003")
#    print(f"My name is {name}, age is {age}")
    print('*'*30)

show01()

show02('Fred',29)

show03('Fred',30)
