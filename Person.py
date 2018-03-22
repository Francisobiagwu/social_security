"""
This is a program used to create a person as well as assign a social security number to them
"""

import hashlib
import random

world_census = {}


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
        self.social_security_number = create_social_security_number()
        world_census[self.social_security_number] = (first_name, last_name)


def create_new_account():
    """
    The create_new_account function takes the last 4 of the social security and uses it to create an
    account number for the user
    :return:
    """


def create_social_security_number():
    social_security_hash_database = get_social_security_number_database()

    new_ssn = (random.randint(100000000, 999999999))
    # convert new_ssn to hash
    hash_object = hashlib.sha512(str(new_ssn).encode())
    new_ssn_hash = hash_object.hexdigest()

    while new_ssn_hash in social_security_hash_database:  # if the social security number exist create a new one
        new_ssn = (random.randint(100000000, 999999999))
        hash_object = hashlib.sha512(str(new_ssn).encode())
        new_ssn_hash = hash_object.hexdigest()

    # write the newly created social security number to the database
    path = 'social_security_number_hash'

    try:
        with open(path, 'a+') as file:
            file.write(str(new_ssn_hash) + "\n")

        get_social_security_number_database()  # call this function to update the social security number tuple
        return new_ssn

    except FileNotFoundError:
        print('We ran into error while fetching the social security database file')


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

        # convert the array to tuple to avoid manipulation of data
        social_security_hash_database = tuple(social_security_hash_database)
        return social_security_hash_database

    except FileNotFoundError:
        print('We ran into error while fetching the social security database file')


def create_default_social_security_number_database():
    path = 'social_security_number_hash'
    random_numbers = set([random.randint(100000000, 999999999) for _ in range(0, 20)])

    try:
        with open(path, 'w') as file:
            for number in random_numbers:
                # numbers was created, but we are going to store the hash in order to save the social security in case
                #  of data breach
                hash_object = hashlib.sha512(str(number).encode())
                file.write(str(hash_object.hexdigest()) + "\n")

            return True
    except FileNotFoundError:
        print('We ran into error trying to write default social security numbers to database')


def get_world_census():
    return world_census
