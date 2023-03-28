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

    html_tmp= """
    <p>Following inputs captures Demographic,real estate and commercial data.These fields are populated with sample values</p>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    year = st.text_input("Year","Type Here")
    Big_Cities = st.text_input("Big Cities","Enter 1 if Big City else 0")
    Other = st.text_input("Other","Enter 1 for cities other than Big Cities else 0")
    st.markdown(html_tmp,unsafe_allow_html=True)
    P1 = st.text_input("P1",3)
    P2 = st.text_input("P2",4)
    P4 = st.text_input("P4",4)
    P5 = st.text_input("P5",5)
    P6 = st.text_input("P6",3)
    P7 = st.text_input("P7",1)
    P11 = st.text_input("P11",2)
    P14 = st.text_input("P14",5)
    P15 = st.text_input("P15",5)
    P17 = st.text_input("P17",5)
    P19 = st.text_input("P19",3)
    P20 = st.text_input("P20",4)
    P21 = st.text_input("P21",4)
    P23 = st.text_input("P23",1)
    P24 = st.text_input("P24",2)
    P25 = st.text_input("P25",0)
    P28 = st.text_input("P28",12.5)
    result=""
    if st.button("Predict"):
        result=predict_revenue(year,Big_Cities,Other,P1,P2,P4,P5,P6,P7,P11,P14,P15,P17,P19,P20,P21,P23,P24,P25,P28)
    st.success('The output is {}'.format(result))

def predict_revenue(year,Big_Cities,Other,P1,P2,P4,P5,P6,P7,P11,P14,P15,P17,P19,P20,P21,P23,P24,P25,P28):
    prediction=model.predict(pd.DataFrame([[year,Big_Cities,Other,P1,P2,P4,P5,P6,P7,P11,P14,P15,P17,P19,P20,P21,P23,P24,P25,P28]]))
    print(prediction)
    return prediction    


if __name__=='__main__':
    main()