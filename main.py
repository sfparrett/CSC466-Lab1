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
  plt.xlabel('Year')
  plt.ylabel('Number of babies named Britney')  
  plt.title("Britney Name Rates")
  plt.show()

def britney_album_sales():
  album_and_sales = pd.DataFrame(data = {
    'Album_sales' : [ 25000000, 000000, 10000000, 3000000, 3100000, 4000000, 1500000, 280000], 
    'year_released' : [1999, 2000, 2001, 2003, 2007,2008, 2011, 2013]})
  plt.plot(album_and_sales['year_released'], album_and_sales['Album_sales'], label = 'Album Sales')
  plt.xticks(np.arange(1998, 2013, 2))
  plt.xlabel('Year')
  plt.ylabel('Count of Album Sales (millions)')  
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
  # get most common biblenames from each year
  # Separate df get church membership for each year (Christian and Catholic)
  
  #names = common_bible_names() if we want 

  #names from "https://en.wikipedia.org/wiki/List_of_biblical_names"
  names = ['Simon', 'Simeon', 'Joseph', 'Joses', 'Lazarus', 'Judas', 'John', 
  'Jesus', 'Ananias', 'Jonathan', 'Matthew', 'Matthias', 'Manaen', 'James',
  'Mary', 'Salome', 'Shelamzion', 'Martha', 'Joanna', 'Sapphira', 'Berenice',
  'Imma', 'Mara', 'Cyprus', 'Sarah', 'Alexandra'
  ]

  overall = []
  for name in names:
    index = df.loc[df['Name']==name]
    overall.append(index)


  finish = pd.concat(overall, sort=False).reset_index()
  
  df1 = finish.groupby(['Name', 'Year'])['Count'].sum().reset_index()

  df = df.groupby(['Name', 'Year'])['Count'].sum().reset_index()

  df1 = (df1.groupby(['Year'])['Count'].sum()/df.groupby(['Year'])['Count'].sum()).reset_index()

  plt.plot(df1['Year'], df1['Count'])
  plt.xlabel('Year')
  plt.ylabel('Percent of Population')  
  plt.title("Biblical Name Rates")
  plt.show()


def trauma(df):
  # Analyze the birth rate of men vs. woman after extreme strife
  # In this case we will be looking at the great depression areas from 1929 - 1933
  g_dep = [1929, 1930, 1931, 1932, 1933]

  for year in g_dep:
    df.drop(df.loc[df['Year']==year].index, inplace=True)
  
  df1 = df.groupby(['Year', 'Gender']).sum().reset_index()

  df1 = df1.pivot_table('Count', ['Year'], 'Gender').reset_index()

  plt.plot(df1['Year'], df1['F'], label = 'Female Birth')
  plt.plot(df1['Year'], df1['M'], label = 'Male Birth')
  plt.xlabel('Year')
  plt.ylabel('Amount of Births (millions)')  
  plt.title("Great Depression Effect on Gender Births")
  plt.legend()
  plt.show()


def catholic_rates():
  catholic_rates = pd.DataFrame(data = {
    'Catholic_Population' : [47900000, 48700000, 50500000,	52300000,	55700000,	57400000, 59900000, 64800000,	65600000, 68100000,	67700000], 
    'Year' : [1970,1975,1980,1985,1990,1995,2000,2005,2010,2015,2020]})
  
  usa_population = pd.DataFrame(data = {
    'Population' : [209513341, 219081251, 229476354,	240499825,	252120309,	265163745, 281710909, 294993511	,	309011475, 320878310, 331002651], 
    'Year' : [1970,1975,1980,1985,1990,1995,2000,2005,2010,2015,2020]})

  overall = catholic_rates['Catholic_Population']/usa_population['Population']

  plt.plot(catholic_rates['Year'], overall)
  plt.xlabel('Year')
  plt.ylabel('Percent of Population')  
  plt.title("Catholic Population Percentage")
  plt.show()


def main():


    parser = argparse.ArgumentParser(description='Analyze data set of baby names.')
    parser.add_argument('--filename')
    args = vars(parser.parse_args())
    csv_file  = args["filename"]
    df = data_cleaning(csv_file)
    #trauma(df)
    #bible(df)
    catholic_rates()
    #britney_names(df)
    #britney_album_sales()

main()