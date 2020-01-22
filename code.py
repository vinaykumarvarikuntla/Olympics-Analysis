# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)

data.rename(columns={'Total':'Total_Medals'}, inplace = True)

data.head(10)

#Code starts here



# --------------
#Code starts here

data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', 'Winter')

data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'],'Both', data['Better_Event'])

better_event = data['Better_Event'].value_counts().index.values[0]
better_event


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

top_countries=top_countries[:-1]

def top_ten (variable1, variable2):
    country_list = []
    country_list= list((variable1.nlargest(10,variable2)['Country_Name']))
    return country_list

top_10_summer = top_ten(top_countries, 'Total_Summer')

top_10_winter = top_ten(top_countries, 'Total_Winter')

top_10 = top_ten(top_countries, 'Total_Medals')

print(top_10_summer)
print(top_10_winter)
print(top_10)

common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print (common)

#common = [set(top_10_summer).intersection(top_10_winter, top_10)]
#print (common)


# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
#print (summer_df)
#plt.figsize(figsize=(20,10))
plt.bar(summer_df['Country_Name'], summer_df['Total_Summer'])
plt.title('Top_10_Summer')
plt.xlabel('Country_Name')
plt.ylabel('Total_Summer')
plt.xticks(rotation=90)

winter_df = data[data['Country_Name'].isin(top_10_winter)]
#print (winter_df)
#plt.figsize(figsize=(20,10))
plt.bar(winter_df['Country_Name'], winter_df['Total_Winter'])
plt.title('Top_10_Winter')
plt.xlabel('Country_Name')
plt.ylabel('Total_Winter')
plt.xticks(rotation=90)

top_df = data[data['Country_Name'].isin(top_10)]
#print (top_10)
#plt.figsize(figsize=(20,10))
plt.bar(top_df['Country_Name'], top_df['Total_Medals'])
plt.title('Top_10')
plt.xlabel('Country_Name')
plt.ylabel('Total_Medals')
plt.xticks(rotation=90)


# --------------
#Code starts here

summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']

summer_max_ratio = max(summer_df['Golden_Ratio'])

summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(), 'Country_Name']


winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']

winter_max_ratio = max(winter_df['Golden_Ratio'])

winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(), 'Country_Name']


top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']

top_max_ratio = max(top_df['Golden_Ratio'])

top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(), 'Country_Name']



# --------------
#Code starts here
data_1 = data[:-1]
data_1.tail()

data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']

data_1['Total_Points'].head()

most_points = max(data_1['Total_Points'])
best_country = data_1.loc[data_1['Total_Points'].idxmax(), 'Country_Name']

print (most_points)
print (best_country)


# --------------
#Code starts here

best = data[data['Country_Name'] == best_country]

best = best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar(stacked = True)

plt.xlabel('United States')

plt.ylabel('Medals Tally')

plt.xticks(rotation = 45)


