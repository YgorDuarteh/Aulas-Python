import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Sales Registration and Dashboard")

st.write("Upload an Excel file with sales data:")

month = st.text_input("Month")

sales = st.number_input("Sales of Month")

if st.button("Save to Excel"):
    try:
        existin_df = pd.read_excel("Planilha_Excel_Test.xlsx")
        new_data = pd.DataFrame({"Month": [month], "Sales": [sales]})
        df = pd.concat([existin_df, new_data], ignore_index=True)
    except FileNotFoundError:
        df = pd.DataFrame({"Month": [month], "Sales": [sales]})
    df.to_excel("Planilha_Excel_Test.xlsx", index=False)
    st.success("Data saved to Planilha_Excel_Test.xlsx") 

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