import pandas as pd
print(pd.__version__)

#DataFrame，您可以将它想象成一个关系型数据表格，其中包含多个行和已命名的列。
#Series，它是单一列。DataFrame 中包含一个或多个 Series，每个 Series 均有一个名称。
city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
print(city_names)
population = pd.Series([852469, 1015785, 485199])
print(population)
pd.DataFrame({ 'City name': city_names, 'Population': population  })
print(pd)

california_housing_dataframe = pd.read_csv("/Volumes/4TUSB3.0/share/data/california_housing_train.csv", sep=",")
california_housing_dataframe.describe()

#访问数据
cities = pd.DataFrame({ 'City name': city_names, 'Population': population  })
print(type(cities['City name']))
print(cities['City name'])

print(type(cities['City name'][1]))
print(cities['City name'][1])

print(type(cities[0:2]))
print(cities[0:2])

#操控数据
print(population / 1000.)

import numpy as np
print(np.log(population))

print(population.apply(lambda val: val > 1000000))

cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']
print(cities)

#practice 1
cities['new bool'] = (cities['Area square miles'] > 50) & cities['City name'].apply(lambda name: name.startswith('San'))
print(cities)

#index
print(city_names.index)
print(cities.index)

print(cities.reindex([2, 0, 1]))
#print(cities)

print(cities.reindex(np.random.permutation(cities.index)))
#print(cities)


#practice 2
print(cities.reindex([2, 0, 4, 1]))




