import re


class PandaAlreadyThere(Exception):
    pass


class Panda:
    def __init__(self, name, email, sex):
        self.name = name
        if not self._is_email_valid(email):
            raise ValueError
        self.email = email
        self.sex = sex.lower()

    def __eq__(self, other):
        return (self.name == other.name
                and self.email == other.email
                and self.sex == other.sex)

    def __hash__(self):
        return hash((self.name, self.email, self.sex))

    def _is_email_valid(self, email):
        pattern = '[\.\w]{1,}[@]\w+[.]\w+'
        if re.match(pattern, email):
            return True
        else:
            return False

    def is_male(self):
        return self.sex == "male"

    def is_female(self):
        return self.sex == "female"

if __name__ == '__main__':
    print(hash(Panda('name', 'e@mail.cc', 'male')))
