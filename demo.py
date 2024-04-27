Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:47) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #1.Given a string, return the string made of its first two chars, so the String "Hello" yields "He".
>>> a="Hello"
>>> print(a[:2])
He
>>> #first_two('abcdefg') → 'ab'
... b='abcdefg'
>>> print(b[:2])
ab
>>> #If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".
... #first_two('ab') → 'ab'
>>> c='ab'
>>> print(c[::])
ab
>>> #2.Given a string, return a new string made of 3 copies of the last 2 chars of the original string. 
... #extra_end('Hello') → 'lololo'
>>> a="hello"
... print(3*(a[-2:]))
lololo
>>> b='ab'
>>> print(3*(b[:]))
ababab
>>> c="hello"
... print(3*(a[-2:]))
SyntaxError: multiple statements found while compiling a single statement
>>> d='Hi'
>>> print(3*(d[:]))
...          
HiHiHi
>>> #Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
... #first_half('WooHoo') → 'Woo'
... e='WooHoo'
...          
>>> print(e[:3])
...          
Woo
>>> #first_half('HelloThere') → 'Hello'
...          
>>> f='Hello there'
...          
>>> print(f[:5])
...          
Hello
>>> #first_half('abcdef') → 'abc'
...          
>>> g='abcdef'
...          
>>> print(g[:3])
...          
abc
        
