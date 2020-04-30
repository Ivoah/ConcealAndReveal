import functools
import operator
import string

'''
Clue #5

For centuries my storm has surged,
To rule with power - my fiercest urge.
My children number seventy nine,
Conceived before the dawn of time.

The greatest of the eight am I,
But third when seen from human eyes.
A year for me is very long,
Twelve times those of earthen homes.

Now take the letters of my name
Convert to positions in the alphabet - the same.
Multiply them all together,
Multiply by the number of my children,
And subtract 176,150,439.
'''

planet = 'Jupiter'.lower()
magic = 176_150_439
more_magic = True
children = 79

vals = [string.ascii_lowercase.index(c) + 1 for c in planet]
print(vals)
n = functools.reduce(operator.mul, vals)*children - magic
print(n)
