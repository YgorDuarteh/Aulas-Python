import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Sales Registration and Dashboard")

st.write("Upload an Excel file with sales data:")

uploaded_file = st.file_uploader("Choose an Excel File", type=["xls", "xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    if "Month" in df.columns and "Sales" in df.columns:
        st.write("### Sales Dashboard")

        fig, ax = plt.subplots()
        ax.pie(df["Sales"], labels=df["Month"], autopct='%1.1f%%', startangle=90,
           colors=['blue', 'green', 'red', 'purple', 'orange'])
        ax.set_title("Monthly Sales Pie Chart")


        st.pyplot(fig)

else:
    st.error("The uploaded file must contain 'Month' and 'Sales' columns.") 