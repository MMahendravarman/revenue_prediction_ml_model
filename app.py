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
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Restaurant Revenue Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    year = st.text_input("Year","Type Here")
    Big_Cities = st.text_input("Big Citie","Type Here")
    Other = st.text_input("Other","Type Here")
    P1 = st.text_input("P1","Type Here")
    P2 = st.text_input("P2","Type Here")
    P4 = st.text_input("P4","Type Here")
    P5 = st.text_input("P5","Type Here")
    P6 = st.text_input("P6","Type Here")
    P7 = st.text_input("P7","Type Here")
    P11 = st.text_input("P11","Type Here")
    P14 = st.text_input("P14","Type Here")
    P15 = st.text_input("P15","Type Here")
    P17 = st.text_input("P17","Type Here")
    P19 = st.text_input("P19","Type Here")
    P20 = st.text_input("P20","Type Here")
    P21 = st.text_input("P21","Type Here")
    P23 = st.text_input("P23","Type Here")
    P24 = st.text_input("P24","Type Here")
    P25 = st.text_input("P25","Type Here")
    P28 = st.text_input("P28","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_revenue(year,Big_Cities,Other,P1,P2,P4,P5,P6,P7,P11,P14,P15,P17,P19,P20,P21,P23,P24,P25,P28)
    st.success('The output is {}'.format(result))

def predict_revenue(year,Big_Cities,Other,P1,P2,P4,P5,P6,P7,P11,P14,P15,P17,P19,P20,P21,P23,P24,P25,P28):
    prediction=model.predict([[year,Big_Cities,Other,P1,P2,P4,P5,P6,P7,P11,P14,P15,P17,P19,P20,P21,P23,P24,P25,P28]])
    print(prediction)
    return prediction    


if __name__=='__main__':
    main()