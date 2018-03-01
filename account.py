
class Person:
    """
    This is a class that creates and instance of a person
    """

    def __init__(self, first_name, last_name):
        """

        :rtype: object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = ""




def create_new_account():
    first_name = str(input("Firstname: "))
    last_name = str(input("Lastname: "))
    date_of_birth = str("Date of birth (MM/DD/YY: ")



    return first_name, last_name, date_of_birth




new_person = Person("Francis", "Obiagwu")
print(new_person.last_name)
