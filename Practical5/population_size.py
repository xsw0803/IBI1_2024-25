import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

uk_countries = {
    'England': 57.11,
    'Wales': 3.13,
    'Northern Ireland': 1.91,
    'Scotland':5.45,
}

china_provinces = {
    'Zhejiang': 65.77,
    'Fujian': 41.88,
    'JIangxi': 45.28,
    'Anhui': 61.27,
    'Jiangsu': 85.15
}

uk_population = []
for i in uk_countries.values():
    uk_population.append(i)
print(sorted(uk_population))

china_population = []
for i in china_provinces.values():
    china_population.append(i)
print(sorted(china_population))

plt.figure()
labels1 = list(uk_countries.keys())
sizes1 = list(uk_countries.values())
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
explode = (0.1, 0, 0, 0)

pie1 = plt.pie(sizes1,
    labels=labels1,
    colors=colors,
    explode=explode,
    autopct='%1.1f%%',
    shadow=True,
    startangle=140,
    pctdistance=0.75,
    textprops={'fontsize': 6},
)
plt.axis('equal')
plt.title('Population distribution of UK provinces')

labels2 = list(china_provinces.keys())
sizes2 = list(china_provinces.values())
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
explode = (0.1, 0, 0, 0, 0)

plt.figure()
pie2 = plt.pie(sizes2,
    labels=labels2,
    colors=colors,
    explode=explode,
    autopct='%1.1f%%',
    shadow=True,
    startangle=140,
    pctdistance=0.75,
    textprops={'fontsize': 6},
)
plt.axis('equal')
plt.title('Population distribution of China provinces')

plt.tight_layout()
plt.show()