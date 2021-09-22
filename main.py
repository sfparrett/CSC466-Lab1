import pandas as pd
import argparse




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

def bible(df):
  # get most common biblenames from each year
  # Separate df get church membership for each year (Christian and Catholic)
  pass


def trauma(df):
  # Analyze the birth rate of men vs. woman after extreme strife
  # In this case we will be looking at the great depression areas from 1929 - 1933
  pass
  g_dep = ['1929', '1930', '1931', '1932', '1933']

  for year in g_dep:
    df.drop(df.loc[df['Year']==year], inplace=True)

  df_final = df.groupby()





def main():
    parser = argparse.ArgumentParser(description='Analyze data set of baby names.')
    parser.add_argument('--filename')
    args = vars(parser.parse_args())
    csv_file  = args["filename"]
    df = data_cleaning(csv_file)

