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


def britney(df):
  print('Sophia rocks and now can do pandas stuff')

  df_with_britney = df[(df['Name']=="Britney") & (df['Gender']=="F")]
  print(df_with_britney)
  # get all the brittney names from the year she was born until present (spelled Britney)
  # maybe make separate df with years /  albums sold ??

def common_bible_names():
  #get bible names from wikipedia return as array 
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

  df1 = df1.groupby(['Year'])['Count'].sum().reset_index()

  print(df1)

  plt.plot(df1['Year'], df1['Count'])
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
    bible(df)

main()