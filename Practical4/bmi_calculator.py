'''
First, get inputs as weight and height, be careful that weight is in kg and height is in m.
Then do the calculate followed as weight/(height**2).

Use if to catelog the number as thin, normal and obesity.
Print the result with a remind.
'''

weight = 55 #kg
height = 1.8 #m

#calculate bmi
bmi = weight/ height**2

#to see whether it's obesity or too thin or not.
if bmi < 18.5:
    print (f"Your bmi is {bmi: .2f}, you're too thin.")
elif bmi > 30.0:
    print (f"Your bmi is {bmi: .2f}, you may have obesity.")
else:
    print (f"Your bmi is {bmi: .2f}, that's great!")

# This input shows the person is too thin.