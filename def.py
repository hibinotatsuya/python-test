def hoge():
    print('hoge')

hoge()

def fuga(str):
    if str == 'fuga':
        print('fuga')
    else:
        print('not fuga')

fuga('fuga')
fuga('hoge')

def add_num(a: int , b: int) -> int: 
    return a + b

print(add_num('1', '2'))

def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

print(test_func(1))
print(test_func(2))
print(test_func(3, [1, 2, 3]))