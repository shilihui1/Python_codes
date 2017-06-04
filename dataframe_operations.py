import pandas as pd
b = pd.read_csv('/Users/lihuishi/Desktop/python codes/dict.csv')
print(b)
# specifying first column is row index
c = pd.read_csv('/Users/lihuishi/Desktop/python codes/dict.csv', index_col = 0)
print(c)

# Print out country column as Pandas Series
print(c['country'])
print(type(c['country']))
# Print out country column as Pandas DataFrame
print(c[['country']])
print(type(c[['country']]))
# Print out DataFrame with country and drives_right columns
print(c[['country', 'capital']])
print(type(c[['country', 'capital']]))

# Print out first 3 observations
print(c[0:3])

# Print out observation for China: loc is label based 
print(c.loc[['CN']])
# Print out observations for India and China
print(c.loc[['IN', 'CN']])
