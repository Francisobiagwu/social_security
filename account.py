"""
This is a program used to create user account and credentials for a user
"""


accounts = {}


class Person:
    """
    This is a class that creates and instance of a person
    """

    def __init__(self, first_name, last_name, date_of_birth):
        """

        :rtype: object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth


def create_new_account():

    def get_first_name():
        first_name = str(input("Firstname: "))
        if len(first_name.strip()) < 2:
            print("Please enter a value for firstname. No space or initials")
            get_first_name()

        return first_name


    def get_last_name():
        last_name = str(input("Lastname: "))
        if len(last_name.strip()) < 2:
            print("Please enter a value for lastname. No space or intials")
            get_last_name()

        return last_name

    def get_date_of_birth():
        birthday = str(input("Date of birth (MM/DD/YY): "))
        if (len(birthday)) != 8:
            print("Please enter a valid value for date")
            get_date_of_birth()

        month = birthday[0:2]
        day = birthday[3:5]
        year = birthday[6:8]

        date_format = False

        if len(month) == 2:
            if len(day) == 2:
                if len(year) == 2:
                    date_format = True

        if not date_format:
            get_date_of_birth()

        return birthday

    first_name = get_first_name()
    last_name = get_last_name()
    date_of_birth = get_date_of_birth()

    username = str(input("Username: "))
    flag = "Unlocked"

    # check if username already exist, if it does, request that the user enters an new username

    accounts[username] = (last_name, first_name, date_of_birth, flag)

    return first_name, last_name, date_of_birth, date_of_birth, flag


create_new_account()
