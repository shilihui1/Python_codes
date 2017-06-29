dict = {
"country": ["Brazil", "Russia", "India", "China", "South Africa"],
"capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "SPretoria"],
"area": [8.516, 17.10, 3.286, 9.597, 1.221],
"population": [200.4, 143.5, 1252, 1357, 52.98]}
print(type(dict))

import pandas as pd
a = pd.DataFrame(dict)
print(type(a))
print(a)
a.index = ['BR', 'RU', 'IN', 'CN', 'SA']
print(a)

print(a.columns)
# one liner code
a['length'] = a['country'].apply(len)

# for loop using a.iterrows()
for label, row in a.iterrows():
    a.loc[label, 'country_length'] = len(row['country'])

print(a)
print(a.columns)
