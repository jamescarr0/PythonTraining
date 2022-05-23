import sys

print("Python main:")
print(f"Argument count: {len(sys.argv)}")
for i, arg in enumerate(sys.argv):
    print(f"Arg {i:>6}: {arg}")