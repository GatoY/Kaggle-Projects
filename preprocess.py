import numpy as np
import matplotlib as plt
import pandas as pd
import re
from sklearn import preprocessing

data = pd.read_csv('train.csv')
data = data.drop(['PassengerId'],axis=1)
min_max_scaler = preprocessing.MinMaxScaler()
data['Pclass'] = pd.DataFrame(min_max_scaler.fit_transform(pd.DataFrame(data['Pclass'])))

data.drop(['Ticket',axis=1])

data['FamilyMembers'] = data['Parch']+data['SibSp']
data['FamilyMembers'] = pd.DataFrame(min_max_scaler.fit_transform(pd.DataFrame(data['FamilyMembers'])))

def get_title(name):
    pattern = r' (\w+)\.'
    result_search = re.search(pattern,name)
    if result_search:
        return result_search.group(1)
    return ''

for dataset in data:
    dataset['Title'] = dataset['Name'].apply(get_title)


for dataset in data:
    dataset['Title'] = dataset['Title'].replace(['Lady', 'Countess','Capt','Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    dataset['Title'] = dataset['Title'].replace('Mlle', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')

data = data.fillna({'Embarked':'S'})

for dataset in data:
    dataset['Sex'] = dataset['Sex'].map({'female':0, 'male':1}).astype(int)
    title_mapping = {'Mr':1, 'Miss':2 , 'Mrs':3, 'Master': 4, 'Rare': 5}
    dataset['Title'] = dataset['Title'].map(title_mapping)
    dataset['Title'] = dataset['Title'].fillna(0)
    dataset['Embarked'] = dataset['Embarked'].map({'S':0, 'C':1, 'Q':2}).astype(int)
    dataset.loc[dataset['Age']<=10, 'Age'] = 0
    dataset.loc[(dataset['Age']>10) & (dataset['Age']<=18)] = 1
    dataset.loc[(dataset['Age']>18) & (dataset['Age']<=60)] = 2
    dataset.loc[(dataset['Age']>60)] = 3
 

