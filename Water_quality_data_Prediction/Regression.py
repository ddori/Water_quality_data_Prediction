import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import numpy as np

# import csv
#
# f = open('data.csv', 'r', encoding='utf-8')
# rdr = csv.reader(f)
# for line in rdr:
#     print(line)
# f.close()


df=pd.read_csv('data.csv')
df.head()

sns.countplot(x='diagnosis', data=df)
plt.show()

df['diagnosis']=df['diagnosis'].replace('M',0)
df['diagnosis']=df['diagnosis'].replace('B',1)
sns.countplot(x='diagnosis', data=df)
plt.show()

### logistic regression , linear regression

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

Y=df['diagnosis']
X=df.iloc[:,2:32]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
log_clf = LogisticRegression()
log_clf.fit(X_train,Y_train)
log_clf.score(X_test, Y_test)
