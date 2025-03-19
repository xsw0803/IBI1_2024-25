import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''
Create a dictionary about input language and popularity.
Print the pupolarity of Python from the dictionary.
Create a dataframe about language and popularity, then put all keys in
dictionary as x, and all values in dictionary as y.
Draw the bar plot and label x as language, label y as percentage of popularity,
the yticks is from 0 to 80, step is 10.
Add text for each y values of each language and show them on the plot.
'''

Language_popularity = {
    'JavaScript': 62.3,
    'HTML': 52.9,
    'Python': 51,
    'SQL': 51,
    'TypeScript': 38.5,
}

print(Language_popularity.get('Python'))

#create a dataframe on language and popularity
df = pd.DataFrame({"Language": Language_popularity.keys(), 
                   "Popularity": Language_popularity.values()})

#put language into x and popularity into y
x = list(Language_popularity.keys())
y = list(Language_popularity.values())

#draw the plot by x,y, color is skyblue and transquency is 1.0
#yticks is from 0 to 80, step is 10
p1 = plt.bar(x, y, color='skyblue', alpha=1.0)
plt.xlabel('Language')
plt.ylabel('Popularity (Percentage)')
plt.title('The percentage poularity of top5 input language')
plt.yticks(range(0,81,10))

#add text for each value. Show them in the bar plot.
for bar in p1:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,  
        height + 1,                         
        str(height),                        
        ha='center',                        
        va='bottom',                        
        fontsize=12
    )

plt.show()