def fizz_buzz(numbers):
    '''
    Given a list of integers:
    1. Replace all integers that are evenly divisble by 3 with "fizz"
    2. Replace all integers divisble by 5 with "buzz"
    3. Replace all integers divisble by both 3 and 5 with "fizzbuzz"

    >>> numbers = [45, 22, 14, 65, 97, 72]
    >>> fizz_buzz(numbers)
    >>> numbers
    ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
    '''

    # Range Solution
    # for i in range(len(numbers)):
    #     n = numbers[i]
    #     if n % 3 == 0:
    #         numbers[i] = "fizz"
    #     if n % 5 == 0:
    #         numbers[i] = "buzz"
    #     if n % 3 == 0 and n % 5 == 0:
    #         numbers[i] = "fizzbuzz"

    # Enumerate solution.
    for i, n in enumerate(numbers):
        if n % 3 == 0:
            numbers[i] = "fizz"
        if n % 5 == 0:
            numbers[i] = "buzz"
        if n % 3 == 0 and n % 5 == 0:
            numbers[i] = "fizzbuzz"