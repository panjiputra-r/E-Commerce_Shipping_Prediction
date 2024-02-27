# import library
import streamlit as st
import pandas as pd
import numpy as np 

# import visualization
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px

def run():
    # Set Title
    st.title('E-COMMERCE SHIPPING VISUALIZATION')

    # memasukkan gambar
    st.image ('https://i.pinimg.com/originals/6f/61/41/6f6141173ae880df302333fcfbe1d0e2.png')

    # markdown
    st.markdown ('---')

    # load data
    st.markdown('<h3 style="text-align:center;">Dataframe</h3>', unsafe_allow_html=True)
    data = pd.read_csv('shippingData.csv')

    # menampilkan dataframe
    st.dataframe(data)
    st.markdown ('---')

    # menampilkan EDA
    st.markdown('## Exploratory Data Analysis (EDA)')

    # Visualisasi Count of Customers by Warehouse Block
    st.markdown ('---')
    st.markdown('### Count of Customers by Warehouse Block')
    plt.figure(figsize=(8, 6))
    sns.countplot(data=data, x='Warehouse_block')
    plt.xlabel('Warehouse Block')
    plt.ylabel('Count')
    st.pyplot(plt)

    # Visualisasi Piechart
    st.markdown ('---')
    st.markdown('### Distribution of Shipments')
    shipment_counts = data['Mode_of_Shipment'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(shipment_counts, labels=shipment_counts.index, autopct='%1.1f%%')
    st.pyplot(fig)

    # Visualisasi histogram
    st.markdown ('---')
    st.markdown('### Distribution Cost of the Product')
    # Membuat histogram
    plt.figure(figsize=(10, 6)) 
    sns.histplot(data=data, x='Cost_of_the_Product', kde=True)
    st.pyplot(plt)

    # Visualisasi Barchart
    st.markdown ('---')
    st.markdown('### Distribution of Customer care calls')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data=data, x='Customer_care_calls', hue='Reached.on.Time_Y.N', ax=ax)
    st.pyplot(fig)


    # Visualisasi Barchart
    st.markdown ('---')
    st.markdown('### Count of Orders by Various Categories')
    # Define the categorical variables to visualize
    visCat = ['Warehouse_block', 'Mode_of_Shipment', 'Product_importance', 'Gender']

    # Create a figure with subplots for each categorical variable
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

    # Plotting multiple bar charts for each categorical variable
    for i, cat in enumerate(visCat):
        sns.countplot(data=data, x=cat, hue='Reached.on.Time_Y.N', ax=axes[i//2, i%2])
        axes[i//2, i%2].set_title(f'Count of Orders by {cat} and On-Time Delivery')

    # Adjust layout
    plt.tight_layout()

    # Display the plot in Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    run()
    