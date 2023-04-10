import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import FastMarkerCluster
from IPython.display import display
import webbrowser

# It will print the smart city index header file in csv format
data = pd.read_csv('F:/Hackathon Project 2023/Smart_City_index_headers.csv')
print(data)

# It will print the world cities details file in csv format
cities = pd.read_csv('F:/Hackathon Project 2023/worldcities.csv')
print(cities)

# It will print the country and continent details in csv format
continents = pd.read_csv('F:/Hackathon Project 2023/country_and_continent.csv')
print(continents)

# Data Prepprocessing
# For smart city index header file

# It will print the data for checking the null values by columns
print(data.isnull().sum())

# It will print the data for checking what columns do i have
print(data.columns)

# There are some spaces of each column head
# Therefore, we need to remove those
dict_rename = {'Smart_Mobility':'Smart_Mobility', 'Smart_Government':'Smart_Government','Smart_Economy':'Smart_Economy'}
data.rename(columns=dict_rename, inplace=True)
print(data)

# For world cities details file

# It will print the cities for checking the null values by columns
print(cities.isnull().sum())

# It will removes rows which has null values
cities.dropna(axis=0, inplace=True)
cities.reset_index(drop=True, inplace=True)
print(cities)

# For country and continent details file

# It will print the country and continent for checking the null values by columns
print(continents.isnull().sum())

# It will removes rows which as null values
continents.dropna(axis=0, inplace=True)
continents.reset_index(drop=True, inplace=True)
print(continents)

# Data Preparation

#  It will Merge two DataFrames
cities_continents = pd.merge(cities,continents, left_on='iso2', right_on='Two_Letter_Country_Code')
print(cities_continents)

# It will Drop unnecessary columns
cities_continents.drop(columns=['city','admin_name','capital','population','id','Continent_Code','Country_Name','Two_Letter_Country_Code','Three_Letter_Country_Code','Country_Number'],inplace=True)
print(cities_continents)

# It will print for checking the null values
print(cities_continents.isnull().sum())

# Visualization

# It will print for checking the unique valuees of continents
print(cities_continents['Continent_Name'].unique())

# Define a variable  in order to filter 'cities_continents'

# So, i defined continent variable as 'Asia'
continent = 'Asia'

# We have too much data on 'cities_continents'
# So, we will figure out continents by continents
cities_continents_filtered = cities_continents[cities_continents['Continent_Name'] == continent]
print(cities_continents_filtered)

# Prepare DataFrame for Visualization
cities_continents_visualization = pd.merge(data, cities_continents_filtered, left_on='City', right_on='city_ascii')
cities_continents_visualization.drop(['Id','SmartCity_Index','SmartCity_Index_relative_Edmonton','city_ascii','country'], axis = 1, inplace=True)
print(cities_continents_visualization)

# Insert "Smart_Total" cokumn in order to compare total index
for i in range(2,8):
    cities_continents_visualization['Smart_Total'] = np.empty(shape=(len(cities_continents_visualization.index),1))
    cities_continents_visualization['Smart_Total'] += cities_continents_visualization.iloc[:,i]
    cities_continents_visualization['Smart_Total']
    print(cities_continents_visualization.columns)
# Relocation of columns


cities_continents_visualization_dict = {'City': cities_continents_visualization['City'],
                                        'Country': cities_continents_visualization['Country'],
                                        'Smart_Mobility ': cities_continents_visualization['Smart_Mobility '],
                                        'Smart_Environment': cities_continents_visualization['Smart_Environment'],
                                        'Smart_Government ': cities_continents_visualization['Smart_Government '],
                                        'Smart_Economy ': cities_continents_visualization['Smart_Economy '],
                                        'Smart_People': cities_continents_visualization['Smart_People'],
                                        'Smart_Living': cities_continents_visualization['Smart_Living'],
                                        'Smart_Total': cities_continents_visualization['Smart_Total'],
                                        'lat': cities_continents_visualization['lat'],
                                        'lng': cities_continents_visualization['lng'],
                                        'iso2': cities_continents_visualization['iso2'],
                                        'iso3': cities_continents_visualization['iso3'],
                                        'Continent_Name': cities_continents_visualization['Continent_Name']}

print(cities_continents_visualization)

# Display Single bar plot
sns.barplot(data=cities_continents_visualization,x='City',y='Smart_Total',palette='pastel')
plt.xticks(rotation=90)
plt.title('City-Total')
plt.show()

# Display Subplot
fig, ((ax1,ax2,ax3), (ax4,ax5,ax6)) = plt.subplots(nrows=2, ncols=3)
fig.suptitle('Smart Index Bar Plot by Each City', fontsize=30)
fig.set_size_inches(18,18)

sns.barplot(data=cities_continents_visualization,x="City",y="Smart_Mobility ",palette='pastel',ax=ax1)
sns.barplot(data=cities_continents_visualization,x="City",y="Smart_Environment",palette='pastel',ax=ax2)
sns.barplot(data=cities_continents_visualization,x="City",y="Smart_Government ",palette='pastel',ax=ax3)
sns.barplot(data=cities_continents_visualization,x="City",y="Smart_Economy ",palette='pastel',ax=ax4)
sns.barplot(data=cities_continents_visualization,x="City",y="Smart_People",palette='pastel',ax=ax5)
sns.barplot(data=cities_continents_visualization,x="City",y="Smart_Living",palette='pastel',ax=ax6)

# Smart_Mobility / ax1
ax1.set(ylabel = 'Smart_Mobility')
ax1.set_title(label="Smart_Mobility", fontdict={'size':20})
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=90)
ax1.set(xlabel=None)

# Smart_Environment / ax2
ax2.set(ylabel='Smart_Environment')
ax2.set_title(label="Smart_Environment", fontdict={'size':20})
ax2.set_xticklabels(ax1.get_xticklabels(), rotation=90)
ax2.set(xlabel=None)

# Smart_Government / ax3
ax3.set(ylabel='Smart_Government')
ax3.set_title(label="Smart_Government", fontdict={'size':20})
ax3.set_xticklabels(ax1.get_xticklabels(), rotation=90)
ax3.set(xlabel=None)

# Smart_Economy / ax4
ax4.set(ylabel='Smart_Economy')
ax4.set_title(label="Smart_Economy", fontdict={'size':20})
ax4.set_xticklabels(ax1.get_xticklabels(), rotation=90)
ax4.set(xlabel=None)

# Smart_People / ax5
ax5.set(ylabel='Smart_People')
ax5.set_title(label="Smart_People", fontdict={'size':20})
ax5.set_xticklabels(ax1.get_xticklabels(), rotation=90)
ax5.set(xlabel=None)

# Smart_Living / ax6
ax6.set(ylabel='Smart_Living')
ax6.set_title(label="Smart_Living", fontdict={'size':20})
ax6.set_xticklabels(ax1.get_xticklabels(), rotation=90)
ax6.set(xlabel=None)

plt.show()

cities_continents_visualization_copy = cities_continents_visualization.copy()
cities_continents_heatmap = cities_continents_visualization_copy.drop(['Country','Smart_Total','lat','lng','iso2','iso3'], axis=1)
print(cities_continents_heatmap)

cities_continents_pivot = cities_continents_visualization_copy.pivot(index='City',columns='Continent_Name')
print(cities_continents_pivot)

# Heatmap
# Reset the index or columns before creating the heatmap
cities_continents_pivot = cities_continents_pivot.reset_index()  # or reset columns

cities_continents_pivot = cities_continents_pivot.fillna(value=np.nan)
cities_continents_pivot = cities_continents_pivot.apply(pd.to_numeric, errors='coerce')
cities_continents_pivot = cities_continents_pivot.select_dtypes(include=[np.number])

plt.figure(figsize=(10, 10))
sns.heatmap(data=cities_continents_pivot, annot=True, annot_kws={"size":10},linewidths=5, cmap="YlGnBu",fmt="")
plt.show()

# Map

# Display a map centered in Asia
map = folium.Map(location=(29, 100), zoom_start=3)

# save the map as an HTML file
map.save('my_map.html')

# open the map in a web browser
webbrowser.open('my_map.html')

print(cities_continents_visualization_copy)

# create a new map object
map = folium.Map(location=[0, 0], zoom_start=2)
# Display Circle Marker on the map
for lat,long,total,radius in zip(cities_continents_visualization_copy['lat'], cities_continents_visualization_copy['lng'], cities_continents_visualization_copy['Smart_Total'], cities_continents_visualization_copy['Smart_Total']):
    folium.CircleMarker(location=[lat,long], radius = radius / 750, fill=True, fill_opacity=0.3,popup=("Total", total)).add_to(map)

# save the map as an HTML file
map.save('circle_map.html')

# open the map in a web browser
webbrowser.open('circle_map.html')


# FastMarkerCluster
FastMarkerCluster(data=cities_continents_visualization_copy[['lat','lng']]).add_to(map)
folium.LayerControl().add_to(map)

# save the map as an HTML file
map.save('fast_marker_cluster_map.html')

# open the map in a web browser
webbrowser.open('fast_marker_cluster_map.html')











