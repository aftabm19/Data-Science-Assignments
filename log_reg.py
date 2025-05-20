# -*- coding: utf-8 -*-
"""
Created on Tue May 20 11:53:44 2025

@author: AFTAB MOMIN
"""

import pickle
import streamlit as st

# Opening model in read binary mode
load = open('log_reg.pkl','rb')
model = pickle.load(load)
 
# Define predict function
def predict(Pclass,Sex,Age,SibSp,Parch,Fare,Embarked):
    prediction = model.predict([[Pclass,Sex,Age,SibSp,Parch,Fare,Embarked]])
    return prediction

def main():
    st.title("Passanger's Survival Model" )
    Pclass = st.number_input('Pclass')
    Sex = st.number_input('Sex')
    Age = st.number_input('Age')
    SibSp = st.number_input('SibSp')
    Parch = st.number_input('Parch')
    Fare = st.number_input("Fare")
    Embarked = st.number_input('Embarked')
    
    if st.button('Prediction'):
        result = predict(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)    
        if result == 0:
            st.success('Non survived passanger')
        else:
            st.success('Survived Passanger')
            
if __name__=='__main__':
    main()