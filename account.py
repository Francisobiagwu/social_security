"""
This is a program used to create user account and credentials for a user
"""
import os

path = "account_file"
accounts = {}
account_file_do_exist = False


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
        first_name = str(input("Firstname: ")).strip()
        if len(first_name.strip()) < 2:
            print("Please enter a value for firstname. No space or initials")
            get_first_name()

        return first_name

    def get_last_name():
        last_name = str(input("Lastname: ")).strip()
        if len(last_name.strip()) < 2:
            print("Please enter a value for lastname. No space or intials")
            get_last_name()

        return last_name

    def get_username():
        user_name = str(input("Username: ")).strip()
        return user_name

    def verify_username(user_name):
        while user_name.lower() == firstname.lower() or user_name.lower() == lastname.lower():
            global username
            print("firstname or lastname cannot be used as the username")
            user_name = get_username()

        username = user_name  # assign the accepted username to our global

    firstname = get_first_name()
    lastname = get_last_name()
    username = get_username()
    verify_username(username)  # verify if the user used first or last name as the user name
    flag = "Unlocked"  # a new account is not supposed to be locked

    # check if username already exist, if it does, request that the user enters an new username

    accounts[username] = (flag, lastname, firstname)  # add the newly created account to account dictionary

    # after creating a new account, add it to the account file
    with open(path, 'a+') as file:
        file.write(username + ":" + flag + ":" + firstname + ":" + lastname + "\n")

    return firstname, lastname, flag


def login():
    user_name = input("username: ")
    password = input("password: ")


def read_account_file():
    if os.stat(path).st_size != 0:
        global account_file_do_exist
        account_file_do_exist = True
        with open(path, 'r') as account_file:
            for line in account_file:
                print(line)
                colon = ":"
                try:
                    first_index = line.index(colon)  # first index for colon
                    username = line[:first_index]

                    second_index = line[first_index + 1:].index(colon)  # second index for colon
                    second_index += first_index + 1
                    flag = line[first_index + 1: second_index]

                    third_index = line[second_index + 1:].index(colon)  # third index for colon
                    third_index += second_index + 1
                    first_name = line[second_index + 1:third_index]

                    last_name = line[third_index + 1:]

                    accounts[username] = (flag, first_name, last_name)  # add the names to account dictionary

                    print(accounts.items())

                except ValueError:
                    account_file_do_exist = False
                    print("Something went wrong with the account file. Verify if account file is totally empty")


    else:
        print("The account file is empty")
        menu()


def menu():
    if not account_file_do_exist:
        print("WELCOME to the Library of the Universe")
        print("--------------------------------------")
        create_new_account()
    else:
        try:
            user_input = int(input("WELCOME to the Library of the Universe\n"
                                   "--------------------------------------\n"
                                   "1: Login \n"
                                   "2: Create a new account "))

            if user_input == 1:
                login()

            elif user_input == 2:
                create_new_account()

            else:
                print("Enter 1 for Login or 2 to create a new account")
                menu()

        except ValueError:
            print("Please only integers are allowed!!!")
            menu()


def main():
    read_account_file()
    menu()


if __name__ == "__main__":
    main()
