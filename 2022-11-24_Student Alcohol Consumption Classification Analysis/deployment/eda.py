import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import numpy as np

def run():

    # Creating title
    st.title('Student Alcohol Consumption in Portugal: Planning to Go to a Higher Education?')
    # Description of the page
    st.write('This page is created by Nadia Oktiarsy')
    st.markdown('---')

    # Adding image
    image = Image.open('escola-portugal.jpg')
    st.image(image, caption='Escola Portugal')

    st.markdown('---')

    # Magic syntax
    st.write('''
    #### Overview

    Alcohol's drawbacks to human body has been discussed for many times, from the scope of health, social science, economy, and many others. It is said that the causes of alcohol abuse tend to be peer pressure, fraternity or sorority involvement, and stress. In the scope of adolesences at school, students who abuse alcohol can suffer from health concerns, poor academic performance or legal consequences. This is also a concern for many parents or caregivers, that probabaly students who have been consuming alcohol tend either to continue their study to a higher education or not.

    This prediction is to understand **if students are having an academic problem because of alcohol drinking habits, evaluate them if they have a probability to pass or fail to get a higher education**. This discussion hopefully can be an insight for the related institutions and organization to make a wise regulation of underage alcohol consumption in Portugal.

    Dataset source: https://www.kaggle.com/datasets/uciml/student-alcohol-consumption
    ''')
    st.markdown('---')

    # Show Dataframe
    st.write('''#### Dataset

    There are 395 students evaluated with 33 different characteristics and values as columns.''')
    df= pd.read_csv('https://raw.githubusercontent.com/nadiaoktiarsy/hacktiv8_p0/main/student-mat.csv')
    st.dataframe(df)
    st.markdown('---')

    # Average Overall
    st.write('''#### General Information''')
    describe = df.describe().T
    st.dataframe(describe)
    st.markdown('---')

    ## Create Barplot
    st.write('''#### Number of Students Aiming A Higher Education
    - Yes (aiming)    : 375
    - No (Not aiming) :  20''')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='higher', data=df)
    st.pyplot(fig)

    # Histogram based on users input
    st.write('''#### Histograms''')
    choice = st.selectbox("Choose a column: ", ('school', 'sex', 'failures', 'absences', 'Dalc', 'Walc', 'G1', 'G2', 'G3'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(df[choice], bins=17, kde=True)
    st.pyplot(fig)