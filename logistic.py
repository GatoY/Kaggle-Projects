import numpy as numpy
import pandas as pd
from sklearn import tree
from sklearn import preprocessing
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier
def load_data(file_name):
    data = pd.read_csv(file_name)
    fix_miss_value(data)
    convert_data(data)
    return data

def fix_miss_value(df):
    df.Embarked[df.Embarked.isnull()] = df.Embarked.dropna().mode().values
    # use title to predict na.
    df.Age[df.Age.isnull()]=df.Age.dropna().mean()
    del df['Cabin']

def convert_data(df):
    df.Sex[df['Sex']=='male']=1
    df.Sex[df['Sex']=='female']=0
    df['fare_bin']=pd.qcut(df.Fare,4)
    df['fare_id']=pd.factorize(df.fare_bin)[0]+1
    df['embarked_id']=pd.factorize(df.Embarked)[0]+1

def off_feature_extraction(df):
    new_df = df.drop(['fare_bin', 'Fare', 'PassengerId', 'Name', 'Ticket', 'Fare', 'Embarked', 'fare_bin'], axis=1)
    new_df.columns = [0,1,2,3,4,5,6,7]
    label = new_df[0].values
    feature = new_df.ix[:,1:].values
    return label, feature

def test_feature_extraction(df):
    new_df = df.drop(['fare_bin', 'Fare', 'PassengerId', 'Name', 'Ticket', 'Fare', 'Embarked', 'fare_bin'], axis=1)
    new_df.columns = [0,1,2,3,4,5,6]
    label_data = pd.read_csv('gender_submission.csv')
    label = label_data['Survived'].values
    feature = new_df.ix[:].values
    return label, feature

def off_model_building(feature,label):
    train_feature, test_feature, train_label, test_label = cross_validation.train_test_split(feature, label, test_size=0.3, random_state = 0)
    clf = RandomForestClassifier(random_state=1,n_estimators=150,min_samples_split=4,min_samples_leaf=2)
    clf=clf.fit(train_feature,train_label)
    return clf, test_label,test_feature

if __name__ == "__main__":
    #load data
    train_data = load_data('train.csv')
    test_data = load_data('test.csv')
    #extract feature and label
    Tlabel, Tfeature = off_feature_extraction(train_data)
    Telabel, Tefeature = test_feature_extraction(test_data)
    clf, test_label, test_feature = off_model_building(Tfeature,Tlabel)
    print clf.score(Tefeature,Telabel)
    print clf.score(test_feature,test_label)
