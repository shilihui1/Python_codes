import pandas as pd
b = pd.read_csv('/Users/lihuishi/Desktop/python codes/dict.csv')
print(b)
c = pd.read_csv('/Users/lihuishi/Desktop/python codes/dict.csv', index_col = 0)
print(c)

# Print out country column as Pandas Series
print(c['country'])
print(type(c['country']))
# Print out country column as Pandas DataFrame
print(c[['country']])
print(type(c[['country']]))
