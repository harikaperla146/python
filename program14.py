class Person :
    count = 0
    def __init__(self, name,age, collegename):
        self.name = name
        self.age = age
        self.collegename = collegename
        Person.count += 1
person1 = Person("Harika", 20, "AWEC")
person2 = Person("Perla", 30, "AWEC")
print(Person.count)
print(person1.name)
print(person2.age)
print(person1.collegename)
