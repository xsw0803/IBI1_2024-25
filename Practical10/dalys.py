import os 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/Users/xsw0803/Desktop/Programme/IBI_practicals/IBI1_2024-25/Practical10/")
'''print(os.getcwd())
print(os.listdir())'''

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
'''print(dalys_data.head(5))'''
print(dalys_data.iloc[0:10, 2])

af_year = dalys_data.loc[dalys_data['Entity'] == 'Afghanistan', 'Year']
find_af = []
for i in af_year:
    find_af.append(i)
print(sorted(find_af)[9])

# The tenth year of record in Afghanistan is 1999.

find_1990 = []
for i in dalys_data['Year']:
    if i == 1990:
        judge = True
        find_1990.append(judge)
    else:
        judge = False
        find_1990.append(judge)
year = dalys_data.loc[find_1990, 'Year']
print(dalys_data.loc[year.index, ['Year', 'DALYs']])
'''print(dalys_data.loc[dalys_data['Year'] == 1990, 'DALYs'])'''

uk = dalys_data.loc[dalys_data['Entity'] == 'United Kingdom', ['DALYs', 'Year']]
france = dalys_data.loc[dalys_data['Entity'] == 'France', ['DALYs', 'Year']]
print(f'{uk['DALYs'].mean():.2f}, {france['DALYs'].mean():.2f}')

# UK DALYs is bigger than France.

if uk['DALYs'].mean() > france['DALYs'].mean():
    print('UK DALYs is bigger.')
elif uk['DALYs'].mean() == france['DALYs'].mean():
    print('UK and France DALYs is the same.')
else:
    print('France DALYs is bigger.')

# UK DALYs is bigger than France.

plt.figure(figsize=(8, 6))
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.xticks(uk.Year, rotation = -45)
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYS over time in the UK')

# Additional question soultion.
dalys_1990 = dalys_data.loc[year.index, 'DALYs']
plt.figure(figsize=(8, 5)) 
box = plt.boxplot(dalys_1990)
plt.xticks([1], ['Across countries in 1990'])
plt.yticks(range(20000, 140000, 20000))
plt.ylabel('DALYs')
plt.title('Distribution of DALYs across countries in 1990')
plt.show()

# Second additional question solution.
'''entity = dalys_data.loc[dalys_data['DALYs'] > 650000, 'Entity'].to_string(index = False)
print(f'The country recorded a DALYs greater than 650,000 in a single year is {entity}.')'''
