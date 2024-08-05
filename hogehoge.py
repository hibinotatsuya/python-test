import json

a = '1000'
print(int(a))

data = [{"id": 1}, {"id": 2}]
fp = open('hoge.json', 'w')
#fp.write(json.dumps(data))
json.dump(data, fp)
fp.close()

print(json.dumps(data))

fp = open('hoge.json', 'r')
#data = json.load(fp)
data = json.loads(fp.read())
print(data)

print('---------')

try:
    result = 0 / 10
except ZeroDivisionError as e:
    print(e)
else:
    print('else')
finally:
    print('finally')

print(result)