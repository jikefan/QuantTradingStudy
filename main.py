from jqdatasdk import *

auth('13156553521','Jukuan.179150')

## 1
# df = get_price('000001.XSHE', start_date='2023-03-28', end_date='2024-04-03', frequency='daily', fields=['open', 'close', 'high', 'low', 'volume', 'money', 'factor'])

# print(type(df))

# df.to_csv('000001-XSHE_2023-03-28_2024-04-03.csv', index=True)

# sec = get_all_securities(['stock'])

## 2
# df = get_concepts()
# print(df[df['name'].str.contains("智能")])

# stock_name_list = get_concept_stocks("SC0022", date="2024-04-03")

# for stock in stock_name_list:
#     df = get_price(stock, start_date='2023-03-28', end_date='2024-04-03', frequency='daily', fields=['open', 'close', 'high', 'low', 'volume', 'money', 'factor'])
#     df.to_csv(stock + '_2023-03-28_2024-04-03.csv', index=True)
