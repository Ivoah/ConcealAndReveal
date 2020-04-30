import string

'''
Clue #10

The key to unlocking the phrase you need
Is in a show that was filmed by WQED
It’s the first phrase a Pittsburgh resident would say
at the start of each episode, every weekday

Though this man is no longer around
His decades of cultural influence is easily found
So my advice, for all you clue seekers
Is to think when you feed your fish or put on your sneakers

BAWPBWSQHZICDTUYZNGAQFRFIQPOUJWFSH
'''

ciphertext = 'BAWPBWSQHZICDTUYZNGAQFRFIQPOUJWFSH'.lower()
key = 'itsabeautifuldayinthisneighborhood'

for i, c in enumerate(ciphertext):
    k = key[i%len(key)]
    print(string.ascii_lowercase[(string.ascii_lowercase.index(c) - string.ascii_lowercase.index(k))%26], end='')
print()
