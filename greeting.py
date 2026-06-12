import sys

name = sys.argv[1] if len(sys.argv) > 1 else input("What is your name? ")
print(f"Hello, {name}! Nice to meet you.")
