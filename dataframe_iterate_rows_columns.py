dict = {
"country": ["Brazil", "Russia", "India", "China", "South Africa"],
"capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "SPretoria"],
"area": [8.516, 17.10, 3.286, 9.597, 1.221],
"population": [200.4, 143.5, 1252, 1357, 52.98]}
type(dict)

import pandas as pd
a = pd.DataFrame(dict)
print(type(a))
print(a)
a.index = ['BR', 'RU', 'IN', 'CN', 'SA']
print(a)

# iterate over columns
for key, value in a.items():
    print(key)
    print(value)

#iterate over rows
for row, label in a.iterrows():
    print(row)
    print(label)
