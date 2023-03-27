import streamlit as st

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