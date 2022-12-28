import streamlit as st
import pandas as pd
import requests

def run():
    with st.form(key='form_parameters'):
        st.write('''**About Customers**''')
        seniorcitizen = st.radio('Are you Senior or Non-Senior Citizen?', options=(1, 0), index=1, help='1 - Senior Citizen, 0 - Non-Senior Citizen')
        tenure = st.number_input('How long have you subscribed our service (in months)?', min_value=0, max_value=100, value=1, step=1)
        st.markdown('---')

        st.write('''**Service Subscription**''')
        phoneservice = st.radio('Phone Service', options=('No', 'Yes'), index=1)
        internetservice = st.radio('Internet Service', options=('DSL','Fiber optic','No'), index=1)
        onlinesecurity = st.radio('Online Security', options=('No', 'Yes', 'No internet service'), index=1)
        onlinebackup = st.radio('Online Backup', options=('Yes','No','No internet service'), index=1)
        deviceprotection = st.radio('Device Protection', options=('No', 'Yes', 'No internet service'), index=1)
        techsupport = st.radio('Technical Support', options=('No', 'Yes', 'No internet service'), index=1)
        streamingtv = st.radio('TV Streaming', options=('No', 'Yes', 'No internet service'), index=1)
        streamingmovies = st.radio('Movies Streaming', options=('No', 'Yes', 'No internet service'), index=1)
        st.markdown('---')

        st.write('''**Payment Information**''')
        contract = st.selectbox('The contract term of the customer: ', options=('Month-to-month', 'One year', 'Two year'), index=1)
        paperlessbilling = st.radio('Are you using paperless billing>', options=('Yes', 'No'), index=1)
        paymentmethod = st.selectbox('Payment method: ', options=('Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'))
        monthlycharges = st.number_input('Insert Monthly Charges', min_value=0, max_value=300, value=1, step=1)
        totalcharges = st.number_input('Insert Total Charges', min_value=0, max_value=10000, value=1, step=1)
        st.markdown('---')       


        submitted = st.form_submit_button('Predict')

    # Create new data
    data_inf = {
        'SeniorCitizen': seniorcitizen,
        'tenure': tenure, 
        'PhoneService': phoneservice, 
        'InternetService': internetservice, 
        'OnlineSecurity': onlinesecurity, 
        'OnlineBackup': onlinebackup,
        'DeviceProtection': deviceprotection, 
        'TechSupport': techsupport, 
        'StreamingTV': streamingtv, 
        'StreamingMovies': streamingmovies, 
        'Contract': contract,
        'PaperlessBilling': paperlessbilling,
        'PaymentMethod': paymentmethod,
        'MonthlyCharges': monthlycharges,
        'TotalCharges': totalcharges
    }


    if submitted:
        # Show Inference DataFrame
        st.dataframe(pd.DataFrame([data_inf]))
        print('[DEBUG] Data Inference : \n', data_inf)

        # Predict
        URL = "https://backend-churn-nadiaoktiarsy.koyeb.app/predict"
        r = requests.post(URL, json=data_inf)

        if r.status_code == 200:
            res = r.json()
            st.write('## Prediction : ', res['label_names'])
            print('[DEBUG] Result : ', res)
            print('')
        else:
            st.write('Error with status code ', str(r.status_code))
        

if __name__ == '__main__':
    run()