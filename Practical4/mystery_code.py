# What does this piece of code do?
# Answer: check it will take how many times to let two random numbers (from one to six) equal.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
#run the while loop
while progress>=0:
	#each run add one lap to represent the number of loops
	progress+=1
	#make two random numbers within one to six (not included six).
	first_n = randint(1,6)
	second_n = randint(1,6)
	#if random numbers equal
	if first_n == second_n:
		#then print the number of loops we used
		print(progress)
		#then get out off the while loop
		break

