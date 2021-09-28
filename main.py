import pandas as pd
import argparse
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import requests
from bs4 import BeautifulSoup


def data_cleaning(csv_file):
  #select csv files
  if(csv_file == 'NationalNames.csv'):
    df = pd.read_csv(csv_file)
    final = df[['Name', 'Year', 'Gender', 'Count']].copy()
  elif(csv_file == 'StateNames.csv'):
    df = pd.read_csv(csv_file)
    final = df[['Name', 'Year', 'Gender', 'Count']].copy()
  else:
    print("Invalid CSV name")
    exit()
  return final


def britney_names(df):
  df_with_britney = df[(df['Name']=="Britney") & (df['Gender']=="F") & (df['Year']>1995)]
  plt.plot(df_with_britney['Year'], df_with_britney['Count'], label= "Newborns named Britney")
  plt.xticks(np.arange(1995, 2014, 2))
  plt.title("Britney Name Rates")
  plt.show()

def britney_album_sales():
  album_and_sales = pd.DataFrame(data = {
    'Album_sales' : [ 25000000, 000000, 10000000, 3000000, 3100000, 4000000, 1500000, 280000], 
    'year_released' : [1999, 2000, 2001, 2003, 2007,2008, 2011, 2013]})
  plt.plot(album_and_sales['year_released'], album_and_sales['Album_sales'], label = 'Album Sales')
  plt.xticks(np.arange(1998, 2013, 2))
  plt.title("Britney Album Sales")
  plt.show()


def common_bible_names():
  response = requests.get(
    url="https://en.wikipedia.org/wiki/List_of_biblical_names",
  )
  soup = BeautifulSoup(response.content, 'html.parser')
  title = soup.find_all(id= "")
  print(title)




def bible(df):
  names = ['Simon', 'Simeon', 'Joseph', 'Joses', 'Lazarus', 'Judas', 'John', 
  'Jesus', 'Ananias', 'Jonathan', 'Matthew', 'Matthias', 'Manaen', 'James',
  'Mary', 'Salome', 'Shelamzion', 'Martha', 'Joanna', 'Sapphira', 'Berenice',
  'Imma', 'Mara', 'Cyprus', 'Sarah', 'Alexandra'
  ]

  fertility_rates = [
          4.8,
          4.61,
          4.39,
          4.17,
          3.94,
          3.81,
          3.64,
          3.53,
          3.29,
          3.13,
          2.69,
          2.17,
          2.06,
          2.42,
          3.01,
          3.31,
          3.58,
          3.23,
          2.54,
          2.03,
          1.77,
          1.8,
          1.91,
          2.03,
          2,
          2.04,
          2.06,
  ]


  years_in_question = [item for item in range(1880, 2014, 5)]
  every_5_years_df = df[df['Year'].isin(years_in_question)]

  overall = []
  for name in names:
    index = every_5_years_df.loc[every_5_years_df['Name']==name]
    overall.append(index)

  finish = pd.concat(overall, sort=False).reset_index()
  df1 = finish.groupby(['Name', 'Year'])['Count'].sum().reset_index()
  df1 = df1.groupby(['Year'])['Count'].sum().reset_index()
  df1["Fertility_Rate"] = fertility_rates
  df1['Name_Count/fertility'] = ((df1['Count']/df1['Fertility_Rate'])//1)
  print(df1)

  plt.plot(df1['Year'], df1['Name_Count/fertility'])
  
  plt.title("Biblical Name Rates")
  plt.show()


def trauma(df):
  # Analyze the birth rate of men vs. woman after extreme strife
  # In this case we will be looking at the great depression areas from 29 - 33
  g_dep = [1929, 1930, 1931, 1932, 1933]

  for year in g_dep:
    df.drop(df.loc[df['Year']==year].index, inplace=True)
  
  df1 = df.groupby(['Year', 'Gender']).sum().reset_index()

  df1 = df1.pivot_table('Count', ['Year'], 'Gender').reset_index()

  plt.plot(df1['Year'], df1['F'], label = 'Female Birth')
  plt.plot(df1['Year'], df1['M'], label = 'Male Birth')
  plt.title("Great Depression Effect on Gender Births")
  plt.legend()
  plt.show()




def main():


    parser = argparse.ArgumentParser(description='Analyze data set of baby names.')
    parser.add_argument('--filename')
    args = vars(parser.parse_args())
    csv_file  = args["filename"]
    df = data_cleaning(csv_file)
    #trauma(df)
    #bible(df)
    bible(df)
    # britney_names(df)
    # britney_album_sales()

main()