class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    [Person(element["name"], element["age"]) for element in people]

    for dict_index in people:
        name = dict_index["name"]
        person = Person.people[name]

        wife_name = dict_index.get("wife")
        if wife_name and wife_name in Person.people:
            person.wife = Person.people[wife_name]

        husband_name = dict_index.get("husband")
        if husband_name and husband_name in Person.people:
            person.husband = Person.people[husband_name]

    return [Person.people[name["name"]] for name in people]
