# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 22:57:10 2021

@author: Hp
"""
import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('D:/Downloads/trained_model.sav','rb'))

#creating a function for prediction
def diabetes_prediction(input_data):
    
    input_data = (6,92,92,0,0,19.9,0.188,28)
    #changing input_data into numpy array
    input_data_as_array = np.asarray(input_data)
    #reshape array as we're predicting for one instance
    input_data_reshaped = input_data_as_array.reshape(1,-1)
    #standardized the data as the training data
    #std_data = scaler.transform(input_data_reshaped)
    #print(std_data)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)  #output is list
    
    if(prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
def main():
    
    #giving a title
    st.title('Diabetes Prediction Web APP')
    
    #getting input data from user
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    
    #getting input from user
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('BloodPressure value')
    SkinThickness = st.text_input('SkinThickness value')
    Insulin= st.text_input('Insulin level')
    BMI= st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction value')
    Age = st.text_input('Age of the person')
    
    
    #code for prediction
    diagnosis = ''
    
    #creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()