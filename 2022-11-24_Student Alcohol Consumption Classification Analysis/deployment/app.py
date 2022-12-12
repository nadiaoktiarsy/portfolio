import streamlit as st
import eda
import prediction

navigation = st.sidebar.selectbox('Choose Page:', ('Exploratory Data Analysis (EDA)', 'Prediction (Pass/Fail)'))

if navigation == 'Exploratory Data Analysis (EDA)':
    eda.run()
else:
    prediction.run()