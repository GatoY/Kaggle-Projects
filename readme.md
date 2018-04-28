#Titanic Project
##Introduction


##Feature Engineering on dataset
<table>
<tr>
<th>PassengerId</th>
<th>Survived</th>
<th>Pclass</th>
<th>Name</th>
<th>Sex</th>
<th>Age</th>
<th>SibSp</th>
<th>Parch</th>
<th>Ticket</th>
<th>Fare</th>
<th>Cabin</th>
<th>Embarked</th>
</tr>

<tr>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th>714/891</th>
<th></th>
<th></th>
<th></th>
<th>204/891</th>
<th>889/891</th>
</tr>

<tr>
<th></th>
<th></th>
<th></th>
<th></th>
<th>convert</th>
<th>fix missed</th>
<th></th>
<th></th>
<th></th>
<th>convert to fare_bin, fare_id</th>
<th>fix missed</th>
<th>fix missed, convert</th>
</tr>

<tr>
<th>int64</th>
<th>int64</th>
<th>int64</th>
<th>object</th>
<th>object</th>
<th>float64</th>
<th>int64</th>
<th>int64</th>
<th>object</th>
<th>float64</th>
<th>object</th>
<th>object</th>
</tr>

<tr>
<th></th>
<th>0/1</th>
<th>convert to vector</th>
<th>convert to title</th>
<th>to 0/1</th>
<th>float64</th>
<th>int64</th>
<th>int64</th>
<th>object</th>
<th>float64</th>
<th>object</th>
<th>object</th>
</tr>

</table>

####Operation

1. fix missed values: Embarked, Age, Cabin.
2. convert data: Sex, fare_bin, fare_id, Embarked.

####Pclass
<table>
<tr>
<th>3</th>
<th>2</th>
<th>1</th>
</tr>
<tr>
<th>(1,0,0)</th>
<th>(1,1,0)</th>
<th>(1,1,1)</th>
</tr>
</table>

####Convert 'Name' to 'Title'
#####convert

'Lady', 'Countess','Capt','Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona' 
#####to 

'Rare'

#####convert 'Mlle', 'Ms' to 'Miss'
#####convert 'Mme' to 'Mrs'

<table>
<tr>
<th>No title</th>
<th>Mr</th>
<th>Miss</th>
<th>Mrs</th>
<th>Master</th>
<th>Rare</th>
</tr>
<tr>
<th>(0,0,0,0,0)</th>
<th>(1,0,0,0,0)</th>
<th>(1,1,0,0,0)</th>
<th>(1,1,1,0,0)</th>
<th>(1,1,1,1,0)</th>
<th>(1,1,1,1,1)</th>
</tr>
</table>

What does master mean? Master is a title for an underage male. If a person is under 18, master would be used. Once a person turns 18 and enters adulthood, mister would be used.

--https://writingexplained.org/master-vs-mister-difference

####Connection

* use Title predict Age.

