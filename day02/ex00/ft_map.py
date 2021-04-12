import sys

def ft_map(func,iterat):
    if not callable(func):
        sys.exit("Please enter a function as the first parameter")
    if '__iter__' not in dir(iterat):
        sys.exit("Please enter an iterable object as the second argument")
    result=[]
    for i in iterat:
        result.append(func(i))
    return result


def add_10(num):
    return num+10

numbers=[1,2,3]

print(ft_map(add_10,numbers))