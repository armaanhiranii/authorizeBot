import pandas as pd
import numpy as np


def text_to_funstuff(file):
    
    count = 0
    df = pd.read_csv(file, usecols = ['Transaction ID', 'Invoice Number',
     'Customer First Name', 'Customer Last Name', 'Invoice Description',
      'Submit Date/Time', 'Total Amount', 'Method'], sep='\t')
    df['Name'] = df['Customer First Name'] + " " + df['Customer Last Name']
    df.drop(['Customer First Name', 'Customer Last Name'], axis='columns', inplace = True)
    df['Account#'] = 116740
    df['Account Name'] = 'Main Deposit'
    df['Source'] = 'Authorize.net'
    df['Visa/Mastercard'] = 0
    df['Amex'] = 0
    for letter in df['Method']:
        if letter == 'A':
            df.iloc[count, 11] = df.iloc[count, 4] + df.iloc[count, 11]
            count += 1
        else:
            df.iloc[count, 10] = df.iloc[count, 4] + df.iloc[count, 10]
            count += 1
    df.drop(['Total Amount', 'Method'], axis= 'columns', inplace = True )

    df[['Invoice Number', 'Booking Number']] = df['Invoice Number'].str.split('|', expand=True)
    df[['Conference Name', 'Names']] = df['Invoice Description'].str.split('-', expand=True)
    df['Submit Date/Time'] = pd.to_datetime(df['Submit Date/Time'])
    df['Submit Date/Time'] = df['Submit Date/Time'].dt.strftime('%m-%d-%Y')
    print(df.head())
    
    return df

text_to_funstuff(r"C:\Users\conf.asst5\Downloads\Download20220728-051226.txt")


