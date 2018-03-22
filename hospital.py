__author__ = "Francis Obiagwu"
__email__ = "cyber.francis@comcast.net"
__date__ = 3 / 21 / 2018


from Person import Person

new_baby = Person('Francis', 'Obiagwu')

# prints the firstname, lastname and the last four of ssn
print(new_baby.first_name, new_baby.last_name, str(new_baby.social_security_number)[5:9])



