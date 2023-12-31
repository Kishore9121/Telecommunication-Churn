# -*- coding: utf-8 -*-
"""Churn_updated

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GjZ5OeuuGsQAA3yMb5W_Umffbcuw9zuX
"""

import pandas as pd
import streamlit as st
from imblearn.combine import SMOTEENN
from collections import Counter
from sklearn.ensemble import RandomForestClassifier

st.title('Kishore Model Development \n Telecommunication Churning')
st.sidebar.header('Input Features')

# Update the column names in your input_features() function
def input_features():
    voice_plan = st.sidebar.selectbox('Voice Plan', ('Yes', 'No'))
    voice_messages = st.sidebar.number_input('Insert Number Of Calls')
    intl_plan = st.sidebar.selectbox('International Plan', ('Yes', 'No'))
    day_mins = st.sidebar.number_input('Insert International Charge')
    day_charge = st.sidebar.number_input('Insert Day Charge')
    eve_mins = st.sidebar.number_input('Insert Evening Minutes')
    eve_charge = st.sidebar.number_input('Insert Night Minutes')

    data = {
        'voice_plan': 1 if voice_plan == 'Yes' else 0,
        'voice_messages': voice_messages,
        'intl_plan': 1 if intl_plan == 'Yes' else 0,
        'day_mins': day_mins,
        'day_charge': day_charge,
        'eve_mins': eve_mins,
        'eve_charge': eve_charge
    }

    features = pd.DataFrame(data, index=[0])
    return features

df = input_features()
st.subheader('User Input Features')
st.write(df)

churn = pd.read_csv('final_churn.csv', encoding='utf_8')
x = churn.iloc[:, 0:7]
y = churn.iloc[:, 7]
sm = SMOTEENN()
X, Y = sm.fit_resample(x, y)
RF = RandomForestClassifier()
RF.fit(X, Y)
predict = RF.predict(df)
prediction_probability = RF.predict_proba(df)

st.subheader('Prediction Result')
if prediction_probability[0][1] > 0.5:
    st.write('Likely to Churn')
else:
    st.write('Loyal Customer')

st.subheader('Prediction Probability')
st.write(prediction_probability)

