
class Shipping:
    next_instance_id = 1234

    # there are two ways to define staticmethod
    #   1. @staticmethod decorator
    #   2. @classmethod decorator
    # as a rule of thumb, use @classmethod if you need to refer to any of the class attributes/methods in that
    # and if none, use @staticmethod. In practice, we can move the @staticmethod completely outside the class into
    # module scope.

    # @staticmethod will usually be implementation detail and hence name will most likely preceed with an _


    # The below method generally is not considered to be a good practice as it needs to refer to the class attribute
    # @staticmethod
    # def _get_next_instance_id():
    #     Shipping.next_instance_id += 1
    #     return Shipping.next_instance_id

    @classmethod
    def _get_next_instance_id(cls):
        cls.next_instance_id += 1
        return cls.next_instance_id

    @classmethod
    def create_empty(cls, company):
        return cls(company, content=None)

    def __init__(self, company, content):
        self.id = Shipping._get_next_instance_id()
        self.company = company
        self.content = content


def experiment1():
    s = Shipping("MSG", "Clothes")
    print(s.id)
    t = Shipping.create_empty("SAS")
    print(t.id)


if __name__ == '__main__':
    experiment1()
