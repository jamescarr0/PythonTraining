from collections import Counter, defaultdict

def counter_better(string):
    return Counter(string)

def counter_naive(string):
    counted = defaultdict(int)
    for c in string:
        counted[c]+=1
    sorted_count = sorted(counted, key=lambda k: counted[k], reverse=True)
    return {c:counted[c] for c in sorted_count}

print(counter_naive("hello"))
print(counter_better("hello"))

# most common method to return n most common values.
print(counter_better("hello").most_common(3))
