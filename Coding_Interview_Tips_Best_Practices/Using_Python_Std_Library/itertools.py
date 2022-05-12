import itertools
from timeit import repeat

# Infinte cycle, calling next will cycle through the items in the list
iterator = itertools.cycle([1, 0])

# calling next will return 1 for n times.
# If times is not set, it will be repeated for infinity.
all_ones = itertools.repeat(1, times=3)

# Combinations and permutations of length r
colours = ['red', 'green', 'blue']
print(list(itertools.combinations(colours, r=2))) # Order does not matter, ie red & green and green & red. < Same thing 
print(list(itertools.permutations(colours, r=2))) # Order matters. red & green and green & red is acceptable