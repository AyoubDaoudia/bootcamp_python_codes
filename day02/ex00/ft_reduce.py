import sys

def ft_reduce(func,iterat):
    if not callable(func):
        sys.exit("Please enter a function as the first parameter")
    if '__iter__' not in dir(iterat):
        sys.exit("Please enter an iterable object as the second argument")
    result=iterat[0]
    for i in iterat[1:]:
        result=func(result,i)
    return result


def mul(num1,num2):
    return num1*num2

numbers=[2,3,4,5]

print(ft_reduce(mul,numbers))
