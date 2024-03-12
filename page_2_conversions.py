from deep_translator import GoogleTranslator
from currency_converter import CurrencyConverter
import pandas as pd
from page_1_data_entry import UK_Price
df = pd.read_csv('Master_Template_Upload.csv')
c = CurrencyConverter

def convert_currencies(df):
    df['Fr Price'] = c.convert(UK_Price,'GBP','EUR')
    df['Ca Price'] = c.convert(UK_Price,'GBP','CAD')
    df['De Price'] = df['Fr Price']
    df['Es Price'] = df['Fr Price']
    df['Ita Price'] = df['Fr Price']
    df['Jpn Price'] = c.convert(UK_Price,'GBP','JPY')
    df['Mx Price'] = c.convert(UK_Price,'GBP','MXN')
    df['USA Price'] = c.convert(UK_Price,'GBP','USD')
    df['Au Price'] = c.convert(UK_Price,'GBP','AUD')#check
    df['NI Price'] = UK_Price #check
    df['Se Price'] = c.convert(UK_Price,'GBP','SEK') #check currency
    return df
print(df)
