import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import numpy as np
import joblib
import json

############ SAVING AND LOADING MODEL ############

# Load all model files
with open('logreg_gridcv.pkl', 'rb') as file_1:
  log_model = joblib.load(file_1)

############ CREATING FORM STREAMLIT ############
st.set_page_config(
        page_title="Student Alcohol Consumption: The Prediction",
        layout='wide',
        initial_sidebar_state='expanded'
    )
    
def run():

    st.title('Student Evaluation Form')

    # Create a Form
    with st.form(key='form_parameters'):
        '''**About Student**'''
        school = st.selectbox(label='School name: ', options=('Gabriel Pereira (GP)', 'Mousinho da Silveira (MS)'), index=1)
        sex = st.radio(label='Gender: ', options=('Female (F)', 'Male (M)'), index=1)
        age = st.number_input('Age: ', min_value=15, max_value=22, value=17, step=1, help='Student age in years (15-22 years old)')
        st.markdown('---')
        '''**Family Information**'''
        Mjob = st.selectbox(label='Mother Job: ', options=('teacher', 'health', 'civil', 'at_home', 'other'), index=1)
        Fjob = st.selectbox(label='Father Job: ', options=('teacher', 'health', 'civil', 'at_home', 'other'), index=1)
        st.markdown('---')

        '''**School Life Habits**'''
        studytime = st.selectbox(label='Study Time per week: ', options=('1', '2', '3', '4'), help=('Study time per week: (1) < 2 hours, (2) 2-5 hours, (3) 5-10 hours, (4) > 10 hours'),index=1)
        failures = st.slider('Failures from the past class: ', 1, 4, 1, help='Please select 4 if more than 3 failures')
        schoolsup = st.radio('Extra educational support: ', options=('yes', 'no'), index=1)
        famsup = st.radio('Family educational support: ', options=('yes', 'no'), index=1)
        paid = st.radio('Extra paid classes within the course subject (Math): ', options=('yes', 'no'), index=1)
        st.markdown('---')
        
        '''**Alcohol Consumption Habits**'''
        Dalc = st.radio('Workday alcohol consumption frequency: ', options=('1', '2', '3', '4', '5'), index=1, help='1 - very low to 5 - very high')
        Walc = st.radio('Weekend alcohol consumption frequency: ', options=('1', '2', '3', '4', '5'), index=1, help='1 - very low to 5 - very high')
        health = st.radio('Current health: ', options=('1', '2', '3', '4', '5'), index=1, help='1 - very bad to 5 - very good')
        absences = st.number_input('Number of Absences: ', min_value=0, max_value=93, step=1)
        st.markdown('---')

        '''**School Grades (Math Subject)**'''
        G1 = st.number_input('1st Period Grade: ', min_value=0, max_value=20, value=10, step=1, help='Grade between 0 - 20')
        G2 = st.number_input('2nd Period Grade: ', min_value=0, max_value=20, value=10, step=1, help='Grade between 0 - 20')
        G3 = st.number_input('3rd Period Grade: ', min_value=0, max_value=20, value=10, step=1, help='Grade between 0 - 20')
        st.markdown('---')

        submitted = st.form_submit_button('Predict')


    ############ DATA INFERENCE ############

    df_inf = {
        'school': school,
        'sex': sex,
        'age': age,
        'Mjob': Mjob,
        'Fjob': Fjob,
        'studytime': studytime,
        'failures': failures,
        'schoolsup': schoolsup,
        'famsup': famsup,
        'paid': paid,
        'Dalc': Dalc,
        'Walc': Walc,
        'absences': absences,
        'health': health,
        'G1': G1,
        'G2': G2,
        'G3': G3
    }

    df_inf = pd.DataFrame([df_inf])
    st.dataframe(df_inf)

    ########### PREDICTION ###########

    if submitted:
        # Predict target inference
        y_inf = log_model.predict(df_inf)
        
        st.write("Pass (1)/Fail (0): ", (y_inf))