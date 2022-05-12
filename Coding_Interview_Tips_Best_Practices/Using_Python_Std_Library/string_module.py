import string

uppercase_hash = set(string.ascii_uppercase)
uppercase_hash.add(" ")

def is_upper(s):
    return all(c in uppercase_hash for c in s)

s = "HELLO WORLD"
s1 = "Hello World"

print(f"{s} is {'all' if is_upper(s) else 'NOT all'} uppercase")
print(f"{s1} is {'all' if is_upper(s1) else 'NOT all'} uppercase")