Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:47) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.
... 
... #without_end('Hello') → 'ell'
... #without_end('java') → 'av'
... #without_end('coding') → 'odin'
... a='Hello'
>>> print(a[1:4])
ell
>>> b='java'
>>> print(b[1:3])
av
>>> c='coding'
>>> len(c)
6
>>> print(c[1:5])
odin
>>> #Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
... #make_abba('Hi', 'Bye') → 'HiByeByeHi'
... #make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
... #make_abba('What', 'Up') → 'WhatUpUpWhat'
>>> a='Hi'
>>> b='Bye'
>>> ab=a+b
>>> ba=b+a
>>> abba=ab+ba
>>> print(abba)
HiByeByeHi
>>> a='Yo'
>>> b='Alice'
>>> ab=a+b
>>> ba=b+a
>>> abba=ab+ba
>>> print(abba)
YoAliceAliceYo
>>> a='What'
>>> b='Up'
>>> ab=a+b
>>> ba=b+a
>>> abba=ab+ba
>>> print(abba)
WhatUpUpWhat
>>> #Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).
... 
... #combo_string('Hello', 'hi') → 'hiHellohi'
... #combo_string('hi', 'Hello') → 'hiHellohi'
... #combo_string('aaa', 'b') → 'baaab'
>>> a='Hello'
>>> b='hi'
>>> print(b+a+b)
hiHellohi
>>> a='hi'
b='Hello'
print(a+b+a)
hiHellohi
a='aaa'
b='b'
print(b+a+b)
baaab
#Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

#non_start('Hello', 'There') → 'ellohere'
#non_start('java', 'code') → 'avaode'
#non_start('shotl', 'java') → 'hotlava'
a='Hello'
b='There'
print(a[1:]+b[1:])
ellohere
a='java'
b='code'
print(a[1:]+b[1:])
avaode
a='shotl'
b='java'
print(a[1:]+b[1:])
hotlava
