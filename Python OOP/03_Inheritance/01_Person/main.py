from project.person import Person
from project.child import Child


def main():
    person = Person("Peter", 25)
    child = Child("Peter Junior", 5)
    print(person.name)
    print(person.age)
    print(child.__class__.__bases__[0].__name__)


if __name__ == "__main__":
    main()