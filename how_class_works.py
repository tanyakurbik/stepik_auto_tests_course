class Person:
    comparisons = []

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}")

    def change_name(self, name):
        self.name = name

    def compare(self, person):
        Person.comparisons.append((self, person))
        if self.age < person.age:
            print(f"{self.name} is {person.age - self.age} years younger than {person.name}")
        elif self.age == person.age:
            print(f"{self.name} and {person.name} are peers")
        else:
            print(f"{self.name} is {self.age - person.age} years older than {person.name}")

    def __repr__(self):
        return f"{self.name} piska"

    @classmethod
    def show_comparisons(cls):
        print(f"{cls.comparisons=}")


person1 = Person('Ivan', 'Eblan', 45)
person2 = Person('Vova', 'Pupin', 45)

person1.show_comparisons()

person1.display()
person1.change_name('Petya')
person1.display()

person1.compare(person2)
# Ivan is 35 years younger than Vova
person1.show_comparisons()
person2.compare(person1)
# Vova is 35 years older than Ivan

person2.show_comparisons()
person2.compare(person1)
# Vova is 35 years older than Ivan

person2.show_comparisons()
person2.compare(person1)
# Vova is 35 years older than Ivan

person2.show_comparisons()
person2.compare(person1)
# Vova is 35 years older than Ivan

person2.show_comparisons()
person2.compare(person1)
# Vova is 35 years older than Ivan

person2.show_comparisons()
person2.compare(person1)
# Vova is 35 years older than Ivan

person2.show_comparisons()
