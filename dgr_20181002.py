Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> xx=1
>>> type(xx)
<type 'int'>
>>> temp=98.6
>>> type(temp)
<type 'float'>
>>> type(1)
<type 'int'>
>>> type(1.0)
<type 'float'>
>>> print(float(99)+100)
199.0
>>> i=42
>>> type(i)
<type 'int'>
>>> f=float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(10/2)
5
>>> print(9/2)
4
>>> print(99/100)
0
>>> print(10.0/2.0)
5.0
>>> print(99.0/100.0)
0.99
>>> sval='123'
>>> type(sval)
<type 'str'>
>>> print

>>> (
	
>>> print(sval=1)
SyntaxError: invalid syntax
>>> print(sval+1)

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(sval+1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> sval='123'
>>> print(sval+1)

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(sval+1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival=int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival+1)
124
>>> nsv='hello bob'
>>> niv=int(nsv)

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    niv=int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bob'
>>> nam=input('Who are you')
Who are you

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    nam=input('Who are you')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> print('welcome',nam)

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print('welcome',nam)
NameError: name 'nam' is not defined
>>> nam=input('Who are you')
Who are youprint('welcome',nam)


Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    nam=input('Who are you')
  File "<string>", line 1
    print('welcome',nam)
        ^
SyntaxError: invalid syntax
>>> inp=input('europe floor?')
europe floor?
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    inp=input('europe floor?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> nam = input('Who are you?')
Who are you?

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    nam = input('Who are you?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> nam=input('Who are you')
Who are you veronika

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    nam=input('Who are you')
  File "<string>", line 1, in <module>
NameError: name 'veronika' is not defined
>>> nam=raw_input('Who are you')
Who are you veronika
>>> print('welcome',nam)
('welcome', ' veronika')
>>> inp=input('europe floor')
europe floor 

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    inp=input('europe floor')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> inp=raw_input('europe floor')
europe floor 0
>>> usf= int(inp)+1
>>> print('Ūs floor',usf)
('\xc5\xaas floor', 1)
>>> 
>>> # Get the name of the file and open
\
>>> # Get the name of the file and open
>>> name = 
input
('Enter file:')
SyntaxError: invalid syntax
>>> # Get the name of the file and open
>>> name = 
input
('Enter file:')handle = open(name, 'r')
SyntaxError: invalid syntax
>>> # Get the name of the file and open
>>> name=input('Enter file:')
Enter file:

Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    name=input('Enter file:')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> name=raw_input('Enter file:')
Enter file:text
>>> handle=open(name,'ŗ')

Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    handle=open(name,'ŗ')
ValueError: mode string must begin with one of 'r', 'w', 'a' or 'U', not 'ŗ'
>>> handle=open(name,'ŗ')

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    handle=open(name,'ŗ')
ValueError: mode string must begin with one of 'r', 'w', 'a' or 'U', not 'ŗ'
>>> handle=open(name,'r')

Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    handle=open(name,'r')
IOError: [Errno 2] No such file or directory: 'text'
>>> name=raw_input('Enter file:')
Enter file:history_20180925.txt
>>> handle=open(name,'r')
>>> handle
<open file 'history_20180925.txt', mode 'r' at 0x7fd5a5d42e40>
>>> counts=dict()
>>> for line in handle:
	words=line.split()
	for word in words:
		counts[word]=counts.get(word,0)+1
		bigcount=none
		bigword=none
		for word,count in counts.items()
		
SyntaxError: invalid syntax
>>> for word,count in counts.items():
	if bigcount is None or count> bigcount:
		bigword=word
		bigcount=count
		print(bigword,bigcount)
		hours:35
		
SyntaxError: invalid syntax
>>> hours:35
SyntaxError: invalid syntax
>>> hours=35
>>> rate=2.75
>>> pay=hours*rate
>>> print(pay)
96.25
>>> 




