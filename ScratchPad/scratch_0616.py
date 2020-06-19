class Person:
    awesome = True
    def __init__(self, name):
        self.name = name
    
    def call(self):
        print("{} is calling, and has name {}".format(self, self.name))
    
    @classmethod
    def sum(cls, num1, num2):
        print(num1 + num2)

    @staticmethod
    def static_sum(num1, num2):
        print(num1 + num2)



if __name__ == "__main__":
    p1 = Person("Amrit")
    p2 = Person("Lucky")
    p1.call()
    p2.call()
    print(dir(p1))
    print(dir(p2))
    print(dir(Person))
    
