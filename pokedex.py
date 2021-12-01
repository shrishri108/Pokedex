#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('pokedex.csv')

#If value not specified, update data from NaN to some error message
df=df.fillna('Record not Found')



nn=input('Enter Name of Pokemon to get detail : ')
flag=0;
x_cood=df.columns[4:11]
for index,row in df.iterrows():
        if(row[1].lower()==nn.lower()):
            print(row)
            flag=1;
            y_cood=row[4:11]
            plt.bar(x_cood,y_cood,color='Green')
            plt.yticks(range(1,100,5),fontsize="8")
            plt.grid(color="grey",linewidth="0.2")
            plt.title("Here is information for "+row[1])
            plt.show()
            break;
if flag==0:print("No record found. Check name again.")
    

chain=[];
for index,row in df.iterrows():
    chain.append(row['Attack'])
chain.sort()
chain[0:10]

