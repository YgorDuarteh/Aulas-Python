import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Sales Registration and Dashboard")

st.write("Enter the sales values below:")

sales_jan = st.number_input("Sales in January")
sales_feb = st.number_input("Sales in February")
sales_mar = st.number_input("Sales in March")
sales_apr = st.number_input("Sales in April")
sales_may = st.number_input("Sales in May")

if st.button("Charts"):
    st.write('### Sales Dashboard')

    data = {
        "Month": ["January", "February", "March", "April", "May"],
        "Sales": [sales_jan, sales_feb, sales_mar, sales_apr, sales_may]
    }

    df = pd.DataFrame(data)

    fig, ax = plt.subplots()
    ax.plot(df["Month"], df["Sales"], marker='o', linestyle='-' , color='b')
    ax.set_ylabel("Sales Value")
    ax.set_title("Monthly Sales Line Chart")
    ax.grid(True)

    st.pyplot(fig)