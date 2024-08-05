def say_something(word, *args):
    print('word =', word)
    for arg in args:
        print(arg)

say_something('Hi!', 'Mike', 'Nance')

def menu(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

menu(entree='beef', drink='coffee')

d = {
    'entree': 'beef',
    'drink': 'coffee',
}
menu(**d)

def hoge(x, y):
    def fuga():
        return x + y
    return fuga

print(hoge(1, 2))
r = hoge(1, 2)
print(r())
#print(fuga(1, 2))