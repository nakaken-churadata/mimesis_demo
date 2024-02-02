from mimesis import Person
from mimesis.locales import Locale
from mimesis.enums import Gender
person = Person(Locale.JA)

print (person.full_name(gender=Gender.FEMALE))
print (person.full_name(gender=Gender.MALE))
