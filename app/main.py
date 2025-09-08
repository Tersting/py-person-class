class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for dict_index in people:
        name = dict_index["name"]
        age = dict_index["age"]
        Person(name, age)

    for dict_index in people:
        name = dict_index["name"]
        persone = Person.people[name]

        if dict_index.get("wife") is not None:
            wife_name = dict_index["wife"]
            if wife_name in Person.people:
                persone.wife = Person.people[wife_name]

        if dict_index.get("husband") is not None:
            husband_name = dict_index["husband"]
            if husband_name in Person.people:
                persone.husband = Person.people[husband_name]
    return [Person.people[name["name"]] for name in people]
