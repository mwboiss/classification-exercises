## Classification Exercises: Data Preperation functions

import pandas as pd
import numpy as np
import os
from pydataset import data
from env import get_db_url, username, password, host
import acquire

# Using the Iris Data:
# Use the function defined in acquire.py to load the iris data.
# Drop the species_id and measurement_id columns.
# Rename the species_name column to just species.
# Create dummy variables of the species name and concatenate onto the iris dataframe. (This is for practice, we don't always have to encode the target, but if we used species as a feature, we would need to encode it).
# Create a function named prep_iris that accepts the untransformed iris data, and returns the data with the transformations above applied.

def prep_iris():

    iris = get_iris_data()
    
    drop_col = ['species_id','measurement_id']
    iris = iris.drop(columns = drop_col)
    
    iris = iris.rename(columns={'species_name' : 'species'})
    
    dummy_name = pd.get_dummies(iris[['species']])
    iris = pd.concat([iris,dummy_name],axis=1)
    
    return iris


# Using the Titanic dataset
# Use the function defined in acquire.py to load the Titanic data.
# Drop any unnecessary, unhelpful, or duplicated columns.
# Encode the categorical columns. Create dummy variables of the categorical columns and concatenate them onto the dataframe.
# Create a function named prep_titanic that accepts the raw titanic data, and returns the data with the transformations above applied.

#titanic = acquire.get_titanic_data()

def prep_titanic(titanic):
    
    
    
    drop_columns = ['class','embarked']
    titanic = titanic.drop(columns=drop_columns)

    dummy_name = pd.get_dummies(titanic[['sex','deck','embark_town']])
    titanic = pd.concat([titanic,dummy_name],axis=1)
    
    return titanic

# Using the Telco dataset
# Use the function defined in acquire.py to load the Telco data.
# Drop any unnecessary, unhelpful, or duplicated columns. This could mean dropping foreign key columns but keeping the corresponding string values, for example.
# Encode the categorical columns. Create dummy variables of the categorical columns and concatenate them onto the dataframe.
# Create a function named prep_telco that accepts the raw telco data, and returns the data with the transformations above applied.

def prep_telco():
    
    telco = get_telco_data()
    
    drop_columns = ['internet_service_type_id','payment_type_id','contract_type_id']
    telco = telco.drop(columns=drop_columns)
    
    dummy_name = pd.get_dummies(telco[['gender','partner','dependents','phone_service','multiple_lines','online_security', 'online_backup','tech_support','streaming_tv', 'streaming_movies','paperless_billing','churn','contract_type','payment_type','internet_service_type']])
    telco = pd.concat([telco,dummy_name],axis=1)
    
    return telco
