a = 15 #walk to bus stop
b = 75 #take the bus
c = a + b #total time for bus method
d = 90 #time to drive
e = 5 #walk to park
f = d + e #total time for car method

if c > f:
    print (f"Car menthod takes {f} mins, is faster!")
elif c == f:
    print ("The same.")
else:
    print (f"Bus method takes {c} mins, is faster!")

# f is longer.
# Walk to bus stop and take the bus is quicker.

X1 = 1==1
Y1 = 1==2
W1 = X1 and Y1 
print (W1)

X2 = 1==1
Y2 = 1==1
W2 = X2 and Y2
print(W2)

X3 = 1==2
Y3 = 1==2
W3 = X3 and Y3
print(W3)

X4 = 1==2
Y4 = 1==1
W4 = X4 and Y4
print(W4)

# if x is true, y is false, w is false.
# if x is true, y is true, w is true.
# if x is false, y is false, w is false.
# if x is false, y is true, w is false.