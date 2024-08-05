def print_info(func):
    print("print_info")
    print(id(func))
    def wrapper(*args, **kwargs):
        print("start")
        print("func:", func.__name__)
        print(id(func))
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper

@print_info
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)