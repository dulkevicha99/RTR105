Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> input
<built-in function input>
>>> input("Cienijamais lietotajs, ludzu, ievadi vienu skaitli: ")
Cienijamais lietotajs, ludzu, ievadi vienu skaitli: 10
10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> mans_mainigums = input("Cienijamais lietotajs, ludzu, ievadi vienu skaitli: ")
Cienijamais lietotajs, ludzu, ievadi vienu skaitli: 10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigums': 10, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> mans_mainigais

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    mans_mainigais
NameError: name 'mans_mainigais' is not defined
>>> mans_mainigums
10
>>> mans_mainigums = input
>>> 
>>> mans_mainigums = input("Cienijamais lietotajs, ludzu, ievadi vienu skaitli: ")
Cienijamais lietotajs, ludzu, ievadi vienu skaitli: 20
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigums': 20, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(mans_mainigums)
<type 'int'>
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigums': 20, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> mans_mainigums = input("Cienijamais lietotajs, ludzu, ievadi vienu skaitli: ")
Cienijamais lietotajs, ludzu, ievadi vienu skaitli: 5
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigums': 5, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/tests_1_20180925.py ===============
Cienijamais lietotajs, ludzu, ievadi skaitli: 5

Traceback (most recent call last):
  File "/home/user/RTR105/tests_1_20180925.py", line 3, in <module>
    x = mans_mainigums * mans_mainigais
NameError: name 'mans_mainigais' is not defined
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/tests_1_20180925.py', 'mans_mainigums': 5, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/tests_1_20180925.py ===============
Cienijamais lietotajs, ludzu, ievadi skaitli: 5
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/tests_1_20180925.py', 'mans_mainigums': 5, '__package__': None, 'x': 25, '__name__': '__main__', '__doc__': None}
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/tests_1_20180925.py', 'mans_mainigums': 5, '__package__': None, 'x': 25, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/tests_1_20180925.py ===============
Cienijamais lietotajs, ludzu, ievadi skaitli: 76
mans_mainigums = 
>>> 
=============== RESTART: /home/user/RTR105/tests_1_20180925.py ===============
Cienijamais lietotajs, ludzu, ievadi skaitli: 57
mans_mainigums = 57
>>> 
=============== RESTART: /home/user/RTR105/tests_1_20180925.py ===============
Cienijamais lietotajs, ludzu, ievadi skaitli: 6
mans_mainigums = 6
vai t esi ievadijis skaitli: = 6
vel atmina tagad ie ari mainigais x= 6
>>> 
=============== RESTART: /home/user/RTR105/tests_1_20180925.py ===============
Cienijamais lietotajs, ludzu, ievadi skaitli: 7
mans_mainigums = 7
vai tu esi ievadijis skaitli: = 7
vel atmina tagad ie ari mainigais x= 49
>>> 
=============== RESTART: /home/user/RTR105/tests_1_20180925.py ===============
Cienijamais lietotajs, ludzu, ievadi skaitli: 45
mans_mainigums = 45
respektīvi, tu esi ievadījis skaitli: = 45
vēl atmiņā tagad ie arī mainīgais x= 2025
>>> 
=============== RESTART: /home/user/RTR105/tests_1_20180925.py ===============
Cienijamais lietotajs, ludzu, ievadi skaitli: 89
mans_mainigums = 89
respektīvi, tu esi ievadījis skaitli: = 89
vēl atmiņā tagad ie arī mainīgais x= 7921
>>> 
=============== RESTART: /home/user/RTR105/tests_1_20180925.py ===============
Cienijamais lietotajs, ludzu, ievadi skaitli: 6
mans_mainigums =      6.000
respektīvi, tu esi ievadījis skaitli: =     6.0000
vēl atmiņā tagad ie arī mainīgais x=      36.0000000
>>> 789
789
>>> 
=============== RESTART: /home/user/RTR105/tests_1_20180925.py ===============
Cienijamais lietotajs, ludzu, ievadi skaitli: 8.6789
mans_mainigums =      8.679
respektīvi, tu esi ievadījis skaitli: =     8.6789
vēl atmiņā tagad ie arī mainīgais x=      75.3233052
>>> 
=============== RESTART: /home/user/RTR105/tests_1_20180925.py ===============
Cienijamais lietotajs, ludzu, ievadi skaitli: 876
mans_mainigums =    876.000
respektīvi, tu esi ievadījis skaitli: =   876.0000
vēl atmiņā tagad ie arī mainīgais x=  767376.0000000
>>> 
=============== RESTART: /home/user/RTR105/tests_1_20180925.py ===============
Cienijamais lietotajs, ludzu, ievadi skaitli: 6986435.9889
mans_mainigums = 6986435.989
respektīvi, tu esi ievadījis skaitli: = 6986435.9889
vēl atmiņā tagad ie arī mainīgais x= 48810287826997.1250000
>>> 
=============== RESTART: /home/user/RTR105/tests_1_20180925.py ===============
Cienijamais lietotajs, ludzu, ievadi skaitli: 6.7
mans_mainigums =      6.700
respektīvi, tu esi ievadījis skaitli: =     6.7000
vēl atmiņā tagad ie arī mainīgais x=      44.8900000
>>> type
<type 'type'>
>>> type(x)
<type 'float'>
>>> type(mans_mainigums)
<type 'float'>
>>> 
=============== RESTART: /home/user/RTR105/tests_1_20180925.py ===============
Cienijamais lietotajs, ludzu, ievadi skaitli: 8
mans_mainigums =      8.000
respektīvi, tu esi ievadījis skaitli: =     8.0000
vēl atmiņā tagad ie arī mainīgais x=      64.0000000
>>> type(mans_mainigais)

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    type(mans_mainigais)
NameError: name 'mans_mainigais' is not defined
>>> 
=============== RESTART: /home/user/RTR105/tests_1_20180925.py ===============
Cienijamais lietotajs, ludzu, ievadi simbolu: ssss

Traceback (most recent call last):
  File "/home/user/RTR105/tests_1_20180925.py", line 3, in <module>
    x = mans_mainigums * mans_mainigums
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/tests_1_20180925.py ===============
Cienijamais lietotajs, ludzu, ievadi simbolu: aaaaa

Traceback (most recent call last):
  File "/home/user/RTR105/tests_1_20180925.py", line 3, in <module>
    x = mans_mainigums * mans_mainigums
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/tests_1_20180925.py ===============
Cienijamais lietotajs, ludzu, ievadi simbolu: aaaa
mans_mainigums = aaaa
respektīvi, tu esi ievadījis skaitli: = aaaa

Traceback (most recent call last):
  File "/home/user/RTR105/tests_1_20180925.py", line 12, in <module>
    print("vēl atmiņā tagad ie arī mainīgais x= %s"%(x))
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR105/tests_1_20180925.py ===============
Cienijamais lietotajs, ludzu, ievadi simbolu: bbb
mans_mainigums = bbb
respektīvi, tu esi ievadījis skaitli: = bbb

Traceback (most recent call last):
  File "/home/user/RTR105/tests_1_20180925.py", line 12, in <module>
    print("vēl atmiņā tagad ie arī mainīgais x= %s"%(x))
NameError: name 'x' is not defined
>>> 

