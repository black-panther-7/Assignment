


import matplotlib.pyplot as plt

import pandas as pd


#Reading data to dataframe


df_tax = pd.read_csv("API_IC.TAX.PAYM_DS2_en_csv_v2_4538353.csv")

print(df_tax)

def bargraphs():

    """ This function reads data from 2018.csv and

    2019.csv and plots number of stolen items(y-axis) """  

    plt.figure()

    plt.bar(df_tax['Country Name'], df_tax['2018'], alpha = 0.5 , label = '2018')

    plt.bar(df_tax['Country Name'], df_tax['2019'], alpha = 0.5 , label = '2019')

    plt.xlabel("<-------Country Name---->")

    plt.ylabel("<------Number------>")

    plt.legend()

    plt.title('Tax payments')

    plt.xticks(rotation=90)

    plt.savefig('bar.png', bbox_inches="tight", dpi = 300)

    plt.show()



def linegraph():

    """ This function reads data from 

    and plots number of incidents(y-axis) vs 

    states in US(x-axis).Visualization method used is """

    plt.figure()

    plt.plot(df_tax['Country Name'], df_tax['2015'], label = '2015')

    plt.plot(df_tax['Country Name'], df_tax['2016'], label = '2016')

    plt.xticks(rotation = 90)

    plt.title('Tax payments in 2015 and 2016')

    plt.legend()

    plt.savefig('line.png', bbox_inches="tight", dpi = 300)

    plt.show()





def piechart():

    """ THis function produces a pie chart for the number of tax payments for the year 2015

    """

    plt.figure()

    plt.pie(df_tax['2015'], labels = df_tax['Country Name'], pctdistance= 1,textprops={'fontsize': 18})

    plt.title('Tax payments in 2015', fontsize = 30)

    plt.savefig('box.png', bbox_inches="tight", dpi = 300)

    plt.show()



#Calling function to plot linegraph

linegraph()



#Calling function to plot bargraph

bargraphs()



#Calling function to plot pie chart

piechart()





