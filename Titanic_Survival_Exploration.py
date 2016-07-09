
import numpy as np
import pandas as pd

from titanic_visualizations import survival_stats
from IPython.display import display
get_ipython().magic(u'matplotlib inline')

in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)
display(full_data.head())

outcomes = full_data['Survived']
data = full_data.drop('Survived', axis = 1)

display(data.head())


def accuracy_score(truth, pred):
    if len(truth) == len(pred): 
        
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)
    
    else:
        return "Number of predictions does not match number of outcomes!"
    
predictions = pd.Series(np.ones(5, dtype = int))
print accuracy_score(outcomes[:5], predictions)


def predictions_0(data):

    predictions = []
    for _, passenger in data.iterrows():
        
        predictions.append(0)
    
    return pd.Series(predictions)

predictions = predictions_0(data)


print accuracy_score(outcomes, predictions)

survival_stats(data, outcomes, 'Sex')


def predictions_1(data):
    
    predictions = []
    for _, passenger in data.iterrows():
        
        
        if passenger['Sex']=="female":
            predictions.append(1)
            
        else:
            predictions.append(0)
    
    return pd.Series(predictions)

predictions = predictions_1(data)



print accuracy_score(outcomes, predictions)



survival_stats(data, outcomes, 'Age', ["Sex == 'male'"])


def predictions_2(data):
    
    predictions = []
    for _, passenger in data.iterrows():
        
        if passenger['Sex']=="female":
            predictions.append(1)
        elif passenger['Sex']=="male" and passenger['Age']<10:
            predictions.append(1)
            
        else:
            predictions.append(0)
    
    return pd.Series(predictions)

predictions = predictions_2(data)



print accuracy_score(outcomes, predictions)


survival_stats(data, outcomes, 'Age', ["Pclass == 2", "Age < 10"])


def predictions_3(data):
    
    predictions = []
    for _, passenger in data.iterrows():
        
        if passenger['Sex']=="female":
            predictions.append(1)
        elif passenger['SibSp'] == 0 and passenger['Age'] < 10 :
            predictions.append(1)
        elif passenger['Fare'] > 200 and passenger['Age'] > 30 and passenger['Age'] < 40:
            predictions.append(1)
        elif passenger['Pclass'] == 2 and passenger['Age'] < 10:
            predictions.append(1)
            
        else:
            predictions.append(0)
    
    return pd.Series(predictions)

predictions = predictions_3(data)


print accuracy_score(outcomes, predictions)