class Attrs:

    def __getattribute__(self, item):
        print("In getattribute: " + item)
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        print("Now in getattr")
        self.__dict__[item] = 'HELLO DAVE'
        return self.__dict__[item]

    def __setattr__(self, key, value):
        print("In setattr: " + ', '.join([key, value]))
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        print("In delattr: " + item)
        object.__delattr__(self, item)


