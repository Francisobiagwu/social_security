__author__ = "Francis Obiagwu"
__email__ = "cyber.francis@comcast.net"
__date__ = 3 / 21 / 2018

import Person

new_baby = Person.Person('Tony', 'Jackson')
immigrant = Person.Person('Bob', 'Smith')

# prints the firstname, lastname and the last four of ssn
print(new_baby.first_name, new_baby.last_name, str(new_baby.social_security_number)[5:9])
print(immigrant.first_name, immigrant.last_name, str(immigrant.social_security_number)[5:9])

print(Person.get_world_census())
