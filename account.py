"""
This is a program used to create user account and credentials for a user
"""

accounts = {}


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

    def get_username():
        user_name = str(input("Username: "))
        return user_name

    def verify_username(username):
        if username == firstname or username == lastname:
            get_username()

    firstname = get_first_name()
    lastname = get_last_name()
    username = get_username()
    flag = "Unlocked"

    # check if username already exist, if it does, request that the user enters an new username

    accounts[username] = (lastname, firstname, flag)

    return firstname, lastname, flag

def login():
    user_name = input("username: ")
    password = input("password: ")







create_new_account()
print(accounts.items())
