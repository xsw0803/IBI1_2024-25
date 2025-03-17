import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Language_popularity = {
    'JavaScript': 62.3,
    'HTML': 52.9,
    'Python': 51,
    'SQL': 51,
    'TypeScript': 38.5,
}

df = pd.DataFrame({"Language": Language_popularity.keys(), 
                   "Popularity": Language_popularity.values()})

x = list(Language_popularity.keys())
y = list(Language_popularity.values())


p1 = plt.bar(x, y, color='skyblue', alpha=1.0)
plt.xlabel('Language')
plt.ylabel('Popularity')
plt.title('The poularity of top5 input language')
plt.yticks(range(0,81,10))

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

print(Language_popularity.get('Python'))