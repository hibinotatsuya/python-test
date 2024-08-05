def hoge():
    yield 'hoge1'
    yield 'hoge2'
    yield 'hoge3'

for i in hoge():
    print(i)
    