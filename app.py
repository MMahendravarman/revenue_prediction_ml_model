import streamlit as st
import pickle
import numpy
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn import linear_model
from matplotlib import pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV

pickle_in = open("revenue_prediction.pkl","rb")
model=pickle.load(pickle_in)

def main():
    st.title('Restaurant Revenue Prediction')
    if st.button("Predict"):
        result=predict_revenue()
    st.success('The output is {}'.format(result))

def predict_revenue():
    prediction=model.predict()
    print(prediction)
    return prediction    


if __name__=='__main__':
    main()