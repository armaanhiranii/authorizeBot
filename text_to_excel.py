import pandas as pd
import numpy as np



def text_to_funstuff(file, excel_file):
    count_refund = 0
    count = 0
    df = pd.read_csv(file, usecols = ['Transaction ID', 'Invoice Number',
     'Customer First Name', 'Customer Last Name', 'Invoice Description',
      'Submit Date/Time', 'Total Amount', 'Method', 'Response Code', 'Action Code', 'Country'], sep='\t')
    
    df.drop(df[df['Response Code'] != 1].index, inplace=True)
    
    for i in df['Action Code']:
         if i == 'CREDIT':
            df.iloc[count_refund, 5] = df.iloc[count_refund, 5] * -1
            count_refund += 1
    print(count_refund)
    print(df['Total Amount'])
    df['Name'] = df['Customer First Name'] + " " + df['Customer Last Name']
    df.drop(['Customer First Name', 'Customer Last Name'], axis='columns', inplace = True)
    df['Account#'] = 116740
    df['Account Name'] = 'Main Deposit'
    df['Source'] = 'Authorize.net'
    df['Visa/Mastercard'] = 0
    df['Amex'] = 0
    # for letter in df['Method']:
    #     if letter == 'A':
    #         df.iloc[count, 11] = df.iloc[count, 4] + df.iloc[count, 11]
    #         count += 1
    #     else:
    #         df.iloc[count, 10] = df.iloc[count, 4] + df.iloc[count, 10]
    #         count += 1
    
    
    df[['Invoice Number', 'Booking Number']] = df['Invoice Number'].str.split('|', expand=True)
    df[['Invoice Description', 'Names']] = df['Invoice Description'].str.split(' - ', expand=True)
    #df['Submit Date/Time'] = pd.to_datetime(df['Submit Date/Time'])
    #df['Submit Date/Time'] = df['Submit Date/Time'].dt.strftime('%m/%d/%Y')
    df.drop(['Total Amount', 'Method', 'Name', 'Invoice Number'], axis= 'columns', inplace = True )
    
    final_df = df.reindex(['Transaction ID','Booking Number','Names',
    'Invoice Description', 'Account#', 'Account Name', 'Source', 
    'Submit Date/Time', 'Visa/Mastercard', 'Amex'], axis=1)

    with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a', if_sheet_exists = 'new') as writer: 
     final_df.to_excel(writer)
    
    
    return final_df


text_to_funstuff(r"C:\Users\conf.asst5\Downloads\Download20220729-062350.txt", r"C:\Users\conf.asst5\Desktop\test.xlsx")