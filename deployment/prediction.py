# import library
import streamlit as st
import pandas as pd
import numpy as np 
import pickle

# load model yang sudah dibuat
with open("model.pkl", "rb") as model:
    model = pickle.load(model)

# function untuk menjalankan streamlit model predictor
def run():
    # Set Title
    st.title('E-COMMERCE SHIPPING PREDICTOR')

    # Sub Title
    st.subheader("This Page Will Focus On The Prediction Of Shipping In E-COMMERCE")
    st.image('https://tecnosoluciones.com/wp-content/uploads/2023/05/estrategias-de-envio-de-productos-para-comercio-electronico.png')

    # Buat Form Input data
    st.markdown('## Input Data')
    with st.form('my_form'):
        Discount_offered = st.number_input('Discount Offered', min_value=0, max_value=100)
        Customer_care_calls = st.number_input('Customer care calls Level', min_value=0, max_value=100)
        Customer_rating = st.selectbox('Customer Rating', options=[1, 2, 3, 4, 5])
        Cost_of_the_Product = st.number_input('Cost of the Product', min_value=0, max_value=999999)
        Warehouse_block = st.selectbox('Warehouse Block', options=['A', 'B', 'C', 'D', 'F'])
        Mode_of_Shipment = st.selectbox('Mode of Shipment', options=['Flight', 'Ship', 'Road'])
        Prior_purchases = st.number_input('Prior Purchases', min_value=0, max_value=100)
        Product_importance = st.selectbox('Product Importance', options=['low', 'medium', 'high'])

        submitted = st.form_submit_button('Lets Check!')

    # dataframe
    data = {
       'Discount_offered' : Discount_offered,
       'Customer_care_calls' : Customer_care_calls,
        'Customer_rating' : Customer_rating,
        'Cost_of_the_Product' : Cost_of_the_Product,
        'Warehouse_block' : Warehouse_block,
        'Mode_of_Shipment' : Mode_of_Shipment,
        'Prior_purchases' : Prior_purchases,
        'Product_importance' : Product_importance,
        }

    df = pd.DataFrame([data])
    st.dataframe(df)
    
    if submitted:
        pred_inf = model.predict(df)

        if pred_inf[0] == 0:
            st.write('REACHED ON TIME')
        else:
            st.write('NOT REACHED ON TIME')

if __name__== '__main__':
    run()

