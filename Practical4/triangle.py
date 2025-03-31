'''
I need a counter to serve as the order of nunmber in the sequence.
And a output as the sequence.

Then, the ordinal number will be bigger in length of 1 for each loop.
The sequence number should plus the last ordinal number to form new sum.

I use while loop, when conuter is smaller than 10, print the sequence numbers.
'''

i = 1 
Tn = 0
#to run the while loop and only give 10 results
while i<= 10 :
    #Tn is the output, each time to add the ordinal numbers of this number.
    Tn += i
    #for each loop, i represent the number of loops
    i += 1
    print (f"The number is {Tn}.")

# Number i represents the first, second, third... figures.
# Answer Tn represents the output of this calculation.