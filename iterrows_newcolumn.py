import pandas as pd
raw_data = [
    {'date': '2013-01-01', 'app': 'iphone', 'num_users': 1000},
    {'date': '2013-01-02', 'app': 'iphone', 'num_users': 1010},
    {'date': '2013-01-03', 'app': 'iphone', 'num_users': 1030},
    {'date': '2013-01-04', 'app': 'iphone', 'num_users': 1050},

    {'date': '2013-01-02', 'app': 'web', 'num_users': 100},
    {'date': '2013-01-03', 'app': 'web', 'num_users': 105},
    {'date': '2013-01-04', 'app': 'web', 'num_users': 110},
    {'date': '2013-01-05', 'app': 'web', 'num_users': 135},
]
a = pd.DataFrame(raw_data)
print(a)
a_iphone = a.groupby(['app']).get_group('iphone')
n = len(a_iphone)
#for i in range(n):
#    a_iphone.loc[i, 'growth_rate'] = a_iphone['num_users'][i]/a_iphone['num_users'][0]
for label, row in a_iphone.iterrows():
    #print(label)
    #print(row)
    newline = a_iphone.loc[label, 'num_users']
    baseline = a_iphone.loc[0, 'num_users']
    a_iphone.loc[label, 'growth_rate'] = newline/baseline
    #a_iphone.loc[label, 'growth_rate'] = a_iphone.loc[label, 'num_users']/a_iphone.loc[0, 'num_users']
print(a_iphone)
