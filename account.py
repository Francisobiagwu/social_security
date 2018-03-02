"""
This is a program used to create user account and credentials for a user
"""
import os

path = "account_file"
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

    accounts[username] = (lastname, firstname, flag)  # add the newly created account to account dictionary

    # after creating a new account, add it to the account file
    with open(path, 'a+') as file:
        file.write(username + ":" + flag + ":" + firstname + ":" + lastname)

    return firstname, lastname, flag


def login():
    user_name = input("username: ")
    password = input("password: ")


def read_account_file():
    if os.stat(path).st_size != 0:
        with open(path, 'r') as account_file:
            for line in account_file:
                print(line)
                colon = ":"
                first_index = line.index(colon)  # first index for colon
                username = line[:first_index]

                second_index = line[first_index + 1:].index(colon)  # second index for colon
                second_index += first_index + 1

                flag = line[first_index + 1: second_index]


                third_index = line[second_index + 1: ].index(colon) # third index for colon

                third_index += second_index + 1
                first_name = line[second_index + 1:third_index]

                last_name = line[third_index + 1:]


                print("firstname: "+first_name)

                print("username: "+username)
                print("flag: "+flag)



    else:
        print("The account file is empty")
        create_new_account()


def main():
    read_account_file()
    login()


if __name__ == "__main__":
    main()
