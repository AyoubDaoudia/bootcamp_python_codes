from ai42.ai42 import loading
from time import sleep

listy = range(1000)
ret = 0
for elem in loading.ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)