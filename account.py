"""
This is a program used to create user account and credentials for a user
"""

import hashlib
import random

persons_created = {}
accounts = {}
account_file_do_exist = False


class Person:
    """
    This is a class that creates an instance of a person
    """

    def __init__(self, first_name, last_name):
        """

        :rtype: object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.social_security_number = 4



def create_new_account():
    """
    The create_new_account function takes the last 4 of the social security and uses it to create an
    account number for the user
    :return:
    """
fffff


def create_social_security_number():
    social_security_hash_database = get_social_security_number_database()
    print(social_security_hash_database)




def get_social_security_number_database():
    """
    Obtains the existing social security numbers from database, verifies that the new
    social security number to be assigned to the user doesn't exist
    :return:
    """
    path = "social_security_number_hash"
    social_security_hash_database = []
    try:
        with open(path, 'r') as file:
            for ssn in file:
                social_security_hash_database.append(ssn.rstrip())

        return social_security_hash_database
    except FileNotFoundError:
        print('We ran into error while fetching the social security database file')



def create_default_social_security_number_database():
    path = 'social_security_number_hash'
    random_numbers = set([random.randint(100000000, 999999999) for _ in range(0, 20)])

    try:
        with open(path, 'w') as file:
            for number in random_numbers:
                # numbers was created, but we are going to store the hash in order to save the social security incase
                #  of data breach
                hash_object = hashlib.sha512(str(number).encode())
                file.write(str(hash_object.hexdigest()) + "\n")

            return True
    except FileNotFoundError:
        print('We ran into error trying to write default social security numbers to database')


create_default_social_security_number_database()
get_social_security_number_database()



