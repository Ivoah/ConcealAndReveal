import string

clue = open('clue0.txt').read()

caesar = lambda s, n=13: ''.join(string.ascii_letters[(string.ascii_letters.index(c) + n)%len(string.ascii_letters)] for c in s)

print(caesar(clue, 4))
