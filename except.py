l = [1, 2, 3]
i = 5

try:
    l[i]
except IndexError as e:
    print('Don\'t worry: {}'.format(e))
finally:
    print('clean up')

print('last')