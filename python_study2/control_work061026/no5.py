name = input()
maxval = 0
try:
    with open(name, 'r') as f:
        for line in f:
            words = len(line.split())
            if words > maxval:
                maxval = words
except FileNotFoundError:
    maxval = 0
print(maxval)