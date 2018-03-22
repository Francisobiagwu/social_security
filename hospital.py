__author__ = "Francis Obiagwu"
__email__ = "cyber.francis@comcast.net"
__date__ = 3 / 21 / 2018

import Person

new_baby = Person.Person('Francis', 'Obiagwu')
another_baby = Person.Person('Bob', 'Smith')

# prints the firstname, lastname and the last four of ssn
print(new_baby.first_name, new_baby.last_name, str(new_baby.social_security_number)[5:9])
print(another_baby.first_name, another_baby.last_name, str(another_baby.social_security_number)[5:9])

print(Person.get_world_census())
