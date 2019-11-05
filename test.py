class Foo(object):
    def __new__(cls, a, b):
        print("Creating Instance")
        return object.__new__(cls)


if __name__ == "__main__":
    i = Foo(2, 3)
