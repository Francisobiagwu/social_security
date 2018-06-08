__author__ = "Francis Obiagwu"
__date__ = 3 / 21 / 2018

from Database import Database, Person


def main():
  """
  This is our main program
  """
  our_database = Database()
  new_baby = Person('Tony', 'Jackson', our_database)
  immigrant = Person('Bob', 'Smith', our_database)
  # prints the firstname, lastname and the last four of ssn
  print(new_baby.first_name, new_baby.last_name, str(new_baby.social_security_number)[5:9])
  print(immigrant.first_name, immigrant.last_name, str(immigrant.social_security_number)[5:9])
  print(our_database.world_census)
  
  
  
if '__name__' == "__main__":
  main()
