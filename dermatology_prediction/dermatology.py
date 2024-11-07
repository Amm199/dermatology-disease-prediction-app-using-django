import pandas as pd
p=pd.read_csv('dermatology.csv')
import pickle
df1=p.drop([' definite borders',' koebner phenomenon', ' polygonal papules', ' follicular papules',' oral mucosal involvement', ' knee and elbow involvement',
       ' scalp involvement', ' family history',' eosinophils in the infiltrate', ' PNL infiltrate',' clubbing of the rete ridges',' follicular horn plug',
       ' perifollicular parakeratosis', ' exocytosis', ' acanthosis',' inflammatory monoluclear inflitrate',' fibrosis of the papillary dermis',' hyperkeratosis',' focal hypergranulosis',
       ' band-like infiltrate'],axis=1)
df1['Age']=df1['Age'].replace('?',34)
x=df1.drop("class",axis=1)
y=df1["class"]
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=10)
from sklearn.ensemble import RandomForestClassifier
model1 = RandomForestClassifier()
mn=model1.fit(X_train,y_train)
pickle.dump(mn,open('derm.pkl','wb'))
