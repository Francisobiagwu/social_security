Social security number is the primary means of identification in United States of America. This is a simple program that generates Social security numbers for new babies born in the hospital. The program starts by importing the social security number database, and then creating a tuple of the social security number hashes. I stored the numbers in hash format to save the user if the database ever gets breached. Then a random social security number is created and then assigned to the new baby. If Before assigning the number to the baby, the program checks to ensure that the number doesn't exist in the database. 

This system hashes the database and then saves the value of the hash on different file. If some reason, the database is tampered with or the file that stores the hash value of the database is tampered with, the system is able to detect this, informs the user and then shuts down. The user of this code can modify it to suit their purpose.





Limitations
---------------
1. The hashing algorithm is not salted, it can be broken with dictionary attack
2. For someone to implement this code in real world, they will have to modify it to include a salt
