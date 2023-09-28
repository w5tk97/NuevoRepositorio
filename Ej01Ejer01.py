(2**3)**2
64
8/(2**3)
1.0
-((8/4)**2)
-4.0
(10**2)/5-((8/4)**2)
16.0
((6+4)/(1+4))**3
8.0
from math import sqrt
5+((7-3)/sqrt((7**2)-(3**3)))
5.852802865422442
-----
foo = "Hello"
bar = 'World!'
foo + bar
'HelloWorld!'
foo-bar
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#13>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'str'
# No se pueden restar cadenas.
foo_bar
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#14>", line 1, in <module>
NameError: name 'foo_bar' is not defined
# foo_bar no es foo+bar, es otra variable nueva.
foo+=" " +bar
'Hello World!'=foo
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
# la variable definida debe estar a la izquierda en lugar de la cadena.
foo =='Hello World!'
True
bar=foo+2*" "
bar += bar
-----
