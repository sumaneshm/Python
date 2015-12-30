
class Shipping:

    next_instance_id = 1234

    HEIGHT_FT = 8.5
    WIDTH_FT = 8

    # there are two ways to define staticmethod
    #   1. @staticmethod decorator
    #   2. @classmethod decorator
    # as a rule of thumb, use @classmethod if you need to refer to any of the class attributes/methods in that
    # and if none, use @staticmethod. In practice, we can move the @staticmethod completely outside the class into
    # module scope.

    # @staticmethod will usually be implementation detail and hence name will most likely preceed with an _


    # The below method generally is not considered to be a good practice as it needs to refer to the class attribute
    # and it is declared as @staticmethod
    # @staticmethod
    # def _get_next_instance_id():
    #     Shipping.next_instance_id += 1
    #     return Shipping.next_instance_id

    @staticmethod
    def _get_bic_code(company, serial):
        return "{}-{}-{}".format(
            company,
            str(serial).zfill(6),    # zfill pads the with preceding zeros
            "U"
        )

    @classmethod
    def _get_next_instance_id(cls):
        cls.next_instance_id += 1
        return cls.next_instance_id

    # @classmethod is inheritance friendly, i.e. cls will automatically call the appropriate __init__ method
    # based on the class being called
    @classmethod
    def create_empty(cls, company, length, *args, **kwargs):
        return cls(company, length, content=None, *args, **kwargs)

    @classmethod
    def create_with_list(cls, company, length, contents, *args, **kwargs):
        return cls(company, length, content=list(contents), *args, **kwargs)

    def __init__(self, company, length_ft, content):
        # here if we call _get_bic_code static method using the class name, it won't be calling the derived
        # class's _get_bic_code static method if it is overridden. To circumvent this problem, we will have to call
        # the static method also using the instance.

        self.bic = self._get_bic_code(
                        company,
                        Shipping._get_next_instance_id())

        self.content = content
        self.length_ft = length_ft


class RefrigeratedShipping(Shipping):

    MAX_CELSIUS = 4

    @staticmethod
    def _get_bic_code(company, serial):
        return "{}-{}-{}".format(
            company,
            serial,
            "R"
        )

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5/9

    def __init__(self, company, length_ft, content, celsius):
        # base class __init__ has to be called "explicitly"
        super().__init__(company, length_ft, content)

        self.celsius = celsius

    # this is how we need to create a property getter
    @property
    def celsius(self):
        return self._celsius

    # use the degree.setter to create its setter
    # degree has got a new decorator called "setter" as it was decorated with "@property"
    @celsius.setter
    def celsius(self, value):
        if value > RefrigeratedShipping.MAX_CELSIUS:
            raise ValueError("Container is too hot...")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = self._f_to_c(value)


def experiment1():
    t = Shipping("MSG", 12, "Utensils")
    print(t.bic)

    t = RefrigeratedShipping("ABC", 12, 'Kitchen', 2)
    print(t.bic)

    # @classmethod is inheritance friendly, i.e. cls will automatically call the appropriate __init__ method
    # based on the class being called
    t = RefrigeratedShipping.create_empty("MSFT", 15, celsius=2)
    print(t)    # t will be an instance of RefrigeratedShipping

    t = Shipping.create_with_list("Google", 10, ["Search engine", "GMail", "Youtube", "Maps"])
    print(t)    # t will be an instance of Shipping

    r = RefrigeratedShipping.create_with_list("Apple", 20, ["iPad", "iPhone", "MacBook Pro"], celsius=3)
    print("Before change : Celsius : {}, Fahrenheit : {}".format(r.celsius, r.fahrenheit))
    r.fahrenheit = 39
    print("After change : Celsius : {}, Fahrenheit : {}".format(r.celsius, r.fahrenheit))



if __name__ == '__main__':
    experiment1()
