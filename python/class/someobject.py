# https://stackoverflow.com/questions/10381967/how-does-the-python-setter-decorator-work

class SomeObject(object):

    def get_test(self):
        return "some value"

    def set_test(self, value):
        print(value)

    test = property(get_test)
    test = test.setter(set_test)
    # OR
    test = property(get_test, set_test)
