class Person(object):
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('Hello, I am a {}'.format(self.name))

    def __del__(self):
        print('Goodbye, I was a {}'.format(self.name))

person = Person('Hibino')
person.say_hello()
