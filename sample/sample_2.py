# from yahoo_fin.stock_info import get_data

# all method
from yahoo_fin.stock_info import *

	
# get_analysts_info('nflx')
# tables = pd.read_html(requests.get(analysts_site, headers=headers).text)

import pandas as pd
import requests

r = requests.get("https://www.sec.gov/Archives/edgar/data/1000229/000095012907000818/h43371ddef14a.htm", headers={'User-agent': 'Mozilla/5.0'}).text
df = pd.read_html(r) #load with user agent to avoid 401 error

df = df[40] #get the right table from the list of dataframes
df = df[8:].rename(columns={i: ' '.join(df[i][:8].dropna()) for i in df.columns}) #generate column headers from the first 8 rows

df.dropna(how='all', axis=1, inplace=True) #remove empty columns and rows
df.dropna(how='all', axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)

def sjoin(x): return ''.join(x[x.notnull()].astype(str))
df = df.groupby(level=0, axis=1).apply(lambda x: x.apply(sjoin, axis=1)) #concatenate columns with the same headers, taken from https://stackoverflow.com/a/24391268/11380795