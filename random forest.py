import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from patsy import dmatrices
from sklearn import metrics
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score
from sklearn import linear_model
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import StandardScaler
train = pd.read_csv('/Users/lihuishi/Desktop/python codes/data_challenge_traindata.csv', index_col = 0)
test = pd.read_csv('/Users/lihuishi/Desktop/python codes/data_challenge_rundata.csv', index_col = 0)

print(type(train))
print(train.shape)
print(train.columns)
print(len(train))
train.head()

print(type(test))
print(test.shape)
print(test.columns)
print(len(test))
test.head()

# how many accounts were won in the training set
win_rate = round(len(train[train['isWon'] == True])/len(train), 3)
print('{} of the account records has been won'.format(win_rate))

# separate the winning accounts and non-winning accounts in the training set
train_win = train[train['isWon'] == True]
train_not_win = train[train['isWon'] == False]
print('The description of the train dataset: ')
print(train.describe())
print('The description of the train dataset with winning records: ')
print(train_win.describe())
print('The description of the train dataset with non-winning records: ')
print(train_not_win.describe())

# how many missing awards
awards_na_rate = round(sum(np.isnan(train['awards']))/len(train), 3)
print('{} of the records has missing awards'.format(awards_na_rate))

# how many missing photos
photos_na_rate = round(sum(np.isnan(train['photos']))/len(train), 3)
print('{} of the records has missing photos'.format(photos_na_rate))

# how many missing clicks
train['clicks'].head()
clicks_na_rate = round(sum(np.isnan(train['clicks']))/len(train), 3)
print('{} of the records has missing clicks'.format(clicks_na_rate))

# for nonclick/click data, how much win rate?
noclick_win = len(train[(np.isnan(train['clicks'])) & (train['isWon'] == True)])
#print(noclick_win)
noclick = len(train[np.isnan(train['clicks'])])
#print(noclick)
noclick_win_rate = round(noclick_win/noclick, 3)
#print(noclick_win_rate)
print('{} out of {} won among nonclick records, with a winning rate of {}'.format(noclick_win, noclick, noclick_win_rate))

click_win = len(train[(train['clicks'] > 0) & (train['isWon'] == True)])
#print(click_win)
click = len(train[train['clicks'] > 0])
#print(click)
click_win_rate = round(click_win/click, 3)
#print(click_win_rate)
print('{} out of {} won among click records, with a winning rate of {}'.format(click_win, click, click_win_rate))

# how many 'timeOnSite' are negative
train_timeOnSite_neg = train[train['timeOnSite'] < 0]
#print(len(train_timeOnSite_neg))
#print(len(train))
timeOnSite_neg_rate = round(len(train_timeOnSite_neg)/len(train), 3)
print('{} out of {}, i.e., {} of the timeOnSite records are negative'.format(len(train_timeOnSite_neg), len(train), timeOnSite_neg_rate))

# plot the mean and median for each factor
feature_list = ['numJobs', 'awards', 'contentCount', 'followers', 
       'freshContent', 'photos', 'starRating', 'clicks',
       'monthOfSignupPageViews', 'intDifficulty', 'intDuration',
       'basePayAmount', 'employeesTotalNum', 'RespondedContacts']

for feature in feature_list:
    print(feature)
    print(train[feature].quantile(0.025))
    print(train[feature].quantile(0.975))
    plt.hist(train[feature], range = [train[feature].quantile(0.025), train[feature].quantile(0.975)])
    plt.show()
    
# plot the mean and median for each factor
feature_list = ['numJobs', 'awards', 'contentCount', 'followers', 
       'freshContent', 'photos', 'starRating', 'clicks',
       'monthOfSignupPageViews', 'intDifficulty', 'intDuration',
       'basePayAmount', 'employeesTotalNum', 'RespondedContacts']

y_pos = np.arange(2)
for feature in feature_list:
    print(feature)

    performance = [train_win[feature].median(), train_not_win[feature].median()]
    plt.xticks(y_pos, ['win', 'not win'])
    plt.ylabel(feature)
    plt.title('Median number of {}'.format(feature))
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.show()

industry_list = train['Industry'].unique()
industry_list = [x for x in industry_list if str(x) != 'nan']
industry_number = []
industry_win_number = []
for industry in industry_list:
    b = len(train[train['Industry'] == industry])
    industry_number.append(b)
    c = len(train[(train['Industry'] == industry) & (train['isWon'] == True)])
    industry_win_number.append(c)
# create a dataframe with industry, number and win_number
industry_table = pd.DataFrame(
    {'industry': industry_list,
     'number': industry_number,
     'win_number': industry_win_number
    })
industry_table['win_rate'] = industry_table['win_number']/industry_table['number']
industry_table = industry_table.sort_values('number', ascending = False)
print(industry_table)

y_pos = np.arange(len(industry_table['industry']))
plt.xticks(y_pos, industry_table['industry'])
plt.ylabel('win_rate')
plt.title('Win rate by industry')
plt.bar(y_pos, industry_table['win_rate'], align='center', alpha=0.5)

x = range(len(industry_table['industry']))
plt.xticks(x,  industry_table['industry'])
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
plt.show()

# the mean and median for each variable split by win and notwin group
print(train.groupby('isWon').mean())
print(train.groupby('isWon').median())

# add "win" column: 1 represents having isWon = True, 0 represents False
train['win'] = (train['isWon'] == True).astype(int)

#y, X = dmatrices('win ~ numJobs + awards + contentCount + followers + freshContent + photos + starRating + clicks\
#       + monthOfSignupPageViews + timeOnSite + intDifficulty + intDuration + C(has_interviews) + basePayAmount + C(subsidiary)\
#       + employeesTotalNum + RespondedContacts',
#                  train, return_type="dataframe")

y, X = dmatrices('win ~ numJobs + awards + contentCount + followers + freshContent + photos + starRating + clicks\
       + monthOfSignupPageViews + timeOnSite + basePayAmount + employeesTotalNum + RespondedContacts',
                  train, return_type="dataframe")

print(X.columns)
y = y.values.ravel()

# instantiate a logistic regression model, and fit with X and y
model = LogisticRegression()
model = model.fit(X, y)

print(model)
print(model.intercept_, model.coef_)

# check the accuracy on the training set
print(model.score(X, y))

# what percentage had won?
print(y.mean())

# evaluate the model by splitting into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
model2 = LogisticRegression()
model2.fit(X_test, y_test)

# predict class labels for the test set
predicted = model2.predict(X_test)
print(predicted)
print(predicted[predicted == 1])

# generate class probabilities
probs = model2.predict_proba(X_test)
print(probs)

# generate evaluation metrics
print(metrics.accuracy_score(y_test, predicted))
print(metrics.roc_auc_score(y_test, probs[:, 1]))

# generate the confusion matrix
print(metrics.confusion_matrix(y_test, predicted))
print(metrics.classification_report(y_test, predicted))

# evaluate the model using 10-fold cross-validation
scores = cross_val_score(LogisticRegression(), X, y, scoring='accuracy', cv=10)
print(scores)
print(scores.mean())

# test dataset
test_features = test[['has_interviews', 'subsidiary', 'numJobs', 'awards', 'contentCount', 'followers', 'freshContent', 'photos', 
                      'starRating', 'clicks', 'monthOfSignupPageViews', 'timeOnSite', 
                      'basePayAmount', 'employeesTotalNum', 'RespondedContacts']]
print(test_features.head())

# change 'subsidiary' from numeric to categorical data
df = test_features['subsidiary']
df = pd.Series(df, dtype="category")
test_features['subsidiary'] = df

# change 'has_interviews' from numeric to categorical data
df = test_features['has_interviews']
df = pd.Series(df, dtype="category")
test_features['has_interviews'] = df

# evaluate the model on test set
X = test_features

# how many missing RespondedContacts
RespondedContacts_na_rate = round(sum(np.isnan(X['RespondedContacts']))/len(X), 3)
print('{} of the records in test dataset has missing RespondedContacts'.format(RespondedContacts_na_rate))

# fill missing values with 0
df = X
df.fillna(0,inplace=True)
X = df
print(X.head())

# 
X_testing = X
X_testing['one'] = 1
cols = X_testing.columns.tolist()
cols = cols[-1:] + cols[:-1]
X_testing = X_testing[cols]
print(X_testing.head())

# predict class labels for the test set
y, X = dmatrices('win ~ numJobs + awards + contentCount + followers + freshContent + photos + starRating + clicks\
       + monthOfSignupPageViews + timeOnSite + C(has_interviews) + basePayAmount + C(subsidiary)\
       + employeesTotalNum + RespondedContacts',
                  train, return_type="dataframe")
print(X.columns)
y = y.values.ravel()

model = LogisticRegression()
model = model.fit(X, y)

print(model)
print(model.intercept_, model.coef_)

# predict class labels for the test set
predicted = model.predict(X_testing)
print(predicted)

# generate class probabilities
probs = model.predict_proba(X_testing)
print(probs)

#print(model)
#print(model.intercept_, model.coef_)

score = probs[:, 1]
print(score)
print(sum(score >= 0.5))
print(score[predicted == 1.0])
print(score[score >= 0.5] )
