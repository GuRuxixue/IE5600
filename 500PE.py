import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime, timedelta
import requests
from lxml import html as HTMLParser
pe_url = 'http://www.multpl.com/table?f=m'
price_url = 'http://www.multpl.com/s-p-500-historical-prices/table/by-month'


def get_data_from_multpl_website(url):
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
        )
    }
    res = requests.get(url, headers=headers)
    parsed = HTMLParser.fromstring(res.content.decode('utf-8'))
    tr_elems = parsed.cssselect('#datatable tr')
    raw_data = [[td.text.strip() for td in tr_elem.cssselect('td')] for tr_elem in tr_elems[1:]]
    return raw_data


pe_data = get_data_from_multpl_website(pe_url)
price_data = get_data_from_multpl_website(price_url)
# merged is the final merged raw data
merged = [[pe_row[0], pe_row[1], price_row[1]] for pe_row, price_row in zip(pe_data, price_data)]
# get first few rows
print(merged[:5])

df = pd.DataFrame(merged, columns=['Date', 'PE', 'Price'])
# parse date formats
df.Date = pd.to_datetime(df.Date, format='%b %d, %Y')
# transform to numeric values
df.PE = pd.to_numeric(df.PE)
df.Price = pd.to_numeric(df.Price.str.replace(',', '').astype(float))  # handle commas inside strings
df = df.set_index('Date')

df1 = df.loc[df.index > datetime(1990, 1, 1)]
df1.is_copy = False
df1.Price = df1.Price / 25

df2 = df.loc[(df.index <= datetime(1990, 1, 1)) & (df.index > datetime(1950, 1, 1))]
df2.is_copy = False
df2.Price = df2.Price / 25

df3 = df.loc[df.index <= datetime(1950, 1, 1)]
df3.is_copy = False
df3.Price = df3.Price

df3.plot()
df2.plot()
df1.plot()
print(np.corrcoef(df3.PE, df3.Price))
print(np.corrcoef(df2.PE, df2.Price))
print(np.corrcoef(df1.PE, df1.Price))
print(np.corrcoef(df.PE, df.Price))