from time import time

def time_random():
 return time() - float(str(time()).split('.')[0])

def gen_random_range(lower = -100000000, upper = 100000000):
 return float(time_random() * (upper - lower) + lower)

print(gen_random_range())
