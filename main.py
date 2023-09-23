#import dependancies
import pandas as pd
import numpy as np
import streamlit as st
import pickle

import warnings
warnings.filterwarnings('ignore')
st.markdown("",unsafe_allow_html=True)

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://wallpapercave.com/wp/wp4339353.jpg");
background-size: cover;
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)

# Loading saved model

model = pickle.load(open('random_search1.pkl','rb'))

def m_prediction(data):
    data1=np.array(data)
    input_data = data1.reshape(1,-1)
    prediction = model.predict(input_data)
    if(prediction[0]==0):
        return "The customer will not churn"
    else:
        return "The customer will churn"


st.title("Telecom Churn Prediction")

#Getting input
account_length = st.slider("Account Length",0,400)

c1,c2=st.columns(2)

with c1:
    voice_plan = st.selectbox("Voice Plan", ["Yes", "No"])
    intl_plan = st.selectbox("International Plan",["Yes","No"])
    intl_calls = st.number_input("Number of international calls",step=1.,format="%.2f")
    day_calls = st.number_input("Number of day calls",step=1.,format="%.2f")
    eve_calls = st.number_input("Number of evening calls",step=1.,format="%.2f")
    night_calls = st.number_input("Number of night calls",step=1.,format="%.2f")
    cust_calls = st.number_input("Number of customer calls", step=1., format="%.2f")

with c2:
    Voice_msg = st.number_input("Number of voice messages",step=1.,format="%.2f")
    intl_min = st.number_input("Number of international minutes",step=1.,format="%.2f")
    day_min = st.number_input("Number of day minutes",step=1.,format="%.2f")
    eve_min = st.number_input("Number of evening minutes",step=1.,format="%.2f")
    night_min = st.number_input("Number of night minutes",step=1.,format="%.2f")
    total_crg = st.number_input("Total Charges",step=1.,format="%.2f")

pred_arr1 = ''
pred_arr = [account_length,voice_plan,Voice_msg,intl_plan,intl_min,intl_calls,day_min,day_calls,eve_min,eve_calls,night_min,night_calls,cust_calls,total_crg]

arr = np.char.replace(pred_arr, 'Yes', '1')
arr1 = np.char.replace(arr, 'No', '0')
arr1 = arr1.astype(np.float)

if st.button("Submit"):
    pred_arr1 = m_prediction(arr1)

st.success(pred_arr1)