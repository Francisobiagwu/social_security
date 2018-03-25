__author__ = "Francis Obiagwu"
__date__ = 10 / 24 / 2016

"""
This is a program used to create social security numbers assigned to individuals
"""

import hashlib
import random
import sys
import os

world_census = {}
path = "social_security_number_hashes" # text file that holds the hash values of the entire population ssn
database_integrity_path = "database_integrity"  # when we hash the database, we store the value of the hash here


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


def create_social_security_number():
    """
    This function creates a new social security number for a person
    :return:
    """
    # Before we create a new social security number, we want to ensure that the storage (database) have not being
    # compromised

    # if the database_integrity_text file is empty, assume the user is running the program for the first time
    if os.stat(database_integrity_path).st_size == 0:
        create_hash, _ = social_security_database_integrity()
        create_hash()
    else:
        _, integrity = social_security_database_integrity()
        integrity = integrity()
        if integrity:
            pass
        else:
            print('Database is compromised, shutting down the system')
            sys.exit(1)

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
    global path

    try:
        with open(path, 'a+') as file:
            file.write(str(new_ssn_hash) + "\n")

        get_social_security_number_database()  # call this function to update the social security number tuple
        create_new_database_hash, _ = social_security_database_integrity()  # we need only create_new_database_hash
        create_new_database_hash()
        return new_ssn

    except FileNotFoundError:
        print('We ran into error while fetching the social security database file')


def get_social_security_number_database():
    """
    Obtains the existing social security numbers from database, verifies that the new
    social security number to be assigned to the user doesn't exist
    :return:
    """

    global path
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
    """
    This function creates a default database filled with social security numbers for testing purposes
    You shouldn't run this function if you already have a database with real social security numbers
    :return:
    """

    global path
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


def social_security_database_integrity():
    """
    We run this program to verify if the social security number hashes have been tampered with by anyone
    :return:
    """
    global path
    global database_integrity_path

    def create_hash_of_database():
        """
        When this function is called, it creates a hash of the social security number database, and then stores it in another file.
        The essence is so that each time the system is rebooted, we always want to verify that someone hasn't tampered with the original file
        :return:
        """

        text_hash = None

        try:
            with open(path, 'r') as file:
                text = file.read()
                text_hash_object = hashlib.sha512(text.encode())
                text_hash = text_hash_object.hexdigest()

        except FileNotFoundError as err:
            print(err.args)

        try:
            with open(database_integrity_path, 'w') as file:
                file.write(str(text_hash))

        except FileNotFoundError as err:
            print(err.args)

    def verify_database_integrity():
        """
        This function verifies if the database have been compromised
        :return:
        """

        last_hash_value = None
        current_hash_value = None

        # get the last saved hash value of the database
        try:
            with open(database_integrity_path, 'r') as file:
                last_hash_value = file.read()

        except FileNotFoundError as err:
            print(err.args)

        # get the current hash value for the database
        try:
            with open(path, 'r') as file:
                text = file.read()
                text_hash_object = hashlib.sha512(text.encode())
                current_hash_value = text_hash_object.hexdigest()

        except FileNotFoundError as err:
            print(err.args)

        # compare the current hash value and the last saved hash value for integrity
        if (current_hash_value == last_hash_value) and (current_hash_value is not None) and (
                last_hash_value is not None):
            return True
        else:
            return False

    return create_hash_of_database, verify_database_integrity


def get_world_census():
    """
    This function returns the entire population
    :return:
    """

    return world_census
