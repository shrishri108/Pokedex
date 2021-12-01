#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('pokedex.csv')

#If value not specified, update data from NaN to some error message
df=df.fillna('Record not Found')

nn=input('Enter Name of Pokemon to get detail : ')
flag=0
this_type="type"
x_cood=df.columns[4:11]
for index,row in df.iterrows():
        if(row[1].lower()==nn.lower()):
            print(row)
            this_type=row['Type 1']
            flag=1;
            plt.subplot(1,2,1)
            y_cood=row[4:11]
            plt.bar(x_cood,y_cood,color='Green')
            plt.yticks(range(1,100,5),fontsize="8")
            plt.xticks(rotation='vertical')
            plt.grid(color="grey",linewidth="0.2")
            plt.title("Here is information for "+row[1])
            plt.plot()
            break;
if flag==0:print("No record found. Check name again.")

chain=[];
for index,row in df.iterrows():
    chain.append(row['Attack'])
chain.sort()
chain[0:10]

#Compare to average values of it's type of pokemon
gby=df.groupby('Type 1').mean()
gby=gby.drop(columns=['#','Legendary'])
gby.head()
gby.loc[this_type]

plt.subplot(1,2,2)
x2cood=df.columns[4:11]
y2cood=gby.loc[this_type][0:7]
plt.bar(x2cood,y2cood,color="Grey")
plt.yticks(range(1,100,5),fontsize="8")
plt.grid(color="grey",linewidth="0.2")
plt.xticks(rotation='vertical')
plt.title("Here is average data for other "+this_type+" type Pokemons.")
#adjust spacing on plots
plt.subplots_adjust(top=0.785,
    bottom=0.255,
    left=0.1,
    right=0.9,
    hspace=0.4,
    wspace=0.54)
plt.plot()
plt.show()