import streamlit as st

st.markdown("""
    <style>
            div.stButton > button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 24px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }
            div.stButton > button:hover {
                background-color: green;
                color: white;
            }
    </style>
""", unsafe_allow_html=True)

st.title("Calculeitor Tabajara")

num1 = st.number_input("Digite o valor 1:")
num2 = st.number_input("Digite o valor 2:"
                       )

col1, col2, col3, col4= st.columns([1, 1, 1, 1])

with col1:
    if st.button("Somar"):
        result= num1 + num2
        st.success(f"A Soma é : {result}!")

with col2:
    if st.button("Multiplicar"):
        result= num1 * num2
        st.success(f"A Multiplicação é : {result}!")

with col3:
    if st.button("Dividir"):
        result= num1 / num2
        st.success(f"A Divisão é : {result}!")

with col4:
    if st.button("Subtrair"):
        result= num1 - num2
        st.success(f"A Subtração é : {result}!")