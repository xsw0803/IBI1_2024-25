import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''
Create a dictionary for uk contries and china provinces to record the areas
and matched population.
List every values of two dictionaries to put population into lists and
print sorted lists.
Draw the first figure as pie chart about uk countries population.
Draw second figure as pie chart about china provinces population.
Show two figures as same time.
'''

#Create dictionary to record countries and matched population.
uk_countries = {
    'England': 57.11,
    'Wales': 3.13,
    'Northern Ireland': 1.91,
    'Scotland':5.45,
}

china_provinces = {
    'Zhejiang': 65.77,
    'Fujian': 41.88,
    'Jiangxi': 45.28,
    'Anhui': 61.27,
    'Jiangsu': 85.15
}

#Get all values in dictionary and put them in the lists.
uk_population = uk_countries.values()
print(sorted(uk_population))

china_population = china_provinces.values()
print(sorted(china_population))

#Draw the first picture as pie chart about uk countries.
plt.figure()
labels1 = list(uk_countries.keys())
sizes1 = list(uk_countries.values())
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
explode = (0.1, 0, 0, 0)

pie1 = plt.pie(sizes1,
    labels=labels1,
    colors=colors,
    explode=explode,
    autopct='%.1f%%',
    shadow=True,
    startangle=140,
    pctdistance=0.75,
    textprops={'fontsize': 6},
)
plt.axis('equal')
plt.title('Population distribution of UK provinces')

labels2 = list(china_provinces.keys())
sizes2 = list(china_provinces.values())
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#66B2FF']
explode = (0.1, 0, 0, 0, 0)

#Draw second figure as pie chart about china provinces.
plt.figure()
pie2 = plt.pie(sizes2,
    labels=labels2,
    colors=colors,
    explode=explode,
    autopct='%.1f%%',
    shadow=True,
    startangle=140,
    pctdistance=0.75,
    textprops={'fontsize': 6},
)
plt.axis('equal')
plt.title('Population distribution of China provinces')

#Automatically adjust and show the pictures.
plt.tight_layout()
plt.show()