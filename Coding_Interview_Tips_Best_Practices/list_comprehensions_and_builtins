lst = [1, 2, -5, 4]

def square(x):
    return x * x


def is_odd(x) -> bool:
    return x % 2 == 1


res = [square(num) for num in lst]
print(res)

res = list(filter(is_odd, lst))
print(res)

res = [num for num in lst if is_odd(num)]
print(res)


# Create a grid using list comprehension
num_cols = 3
num_rows = 4
grid = [ [0 for _ in range(num_cols)] for _ in range(num_rows) ]
print(grid)

### Builtins
print(max(lst)) # maximum int in the list of nums
print(max(lst, key=lambda x: x * x)) # max int which will produce the highest squared number in the list.

# same as above, but will show minimum values, int and smallest square.
print(min(lst))
print(min(lst, key=lambda x: x * x))

## ANY and ALL
# returns true if any values in the list are true
print(any(lst))

# Are any numbers odd?
print(any([(lambda x: x % 2 == 1)(num) for num in lst]))

# Are all the numbers odd?
print(all([(lambda x: x % 2 == 1)(num) for num in lst]))