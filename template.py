import string

s = """\
Hi $name.
$contents
Have a nice day.
"""

t = string.Template(s)
result = t.substitute(name='hibino', contents='Hello World!')

print(result, end='')