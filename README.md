This is a simple program the generates Social security numbers for new babies born in the hospital
The program starts by importing the social security number database, and then creating a tuple of the social security number hashes
I stored the numbers in hash format to save the user if the database ever gets breached.
Then a random social security number is created and then assigned to the new baby. If Before assigning the number to the
baby, the program checks to ensure that the number doesn't exist in the database.





Limitations
---------------
1. The hashing algorithm is not salted, it can be broken with dictionary attack
2. For someone to implement this code in real world, they will have to modify it to include a salt
