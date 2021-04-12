import sys

def ft_filter(func,iterat):
    if not callable(func):
        sys.exit("Please enter a function as the first parameter")
    if '__iter__' not in dir(iterat):
        sys.exit("Please enter an iterable object as the second argument")
    result=[]
    for i in iterat:
        if func(i)== True:
            result.append(i)
    return result


def mod_2(num):
    if num%2==0:
        return True
    return False

numbers=[1,2,3,4,5,6,7,8]

print(ft_filter(mod_2,numbers))
        