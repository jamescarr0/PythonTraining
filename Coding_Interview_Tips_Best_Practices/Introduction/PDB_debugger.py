def max_num(lst):
    num = -float('inf')

    for n in lst:
        breakpoint() # Break here and start python debugger
                     # Step through and use similar to GDB.
        if n > num:
            num = n
    return num

lst = [-3, -1, -9, -2, -5]

print(max_num(lst))