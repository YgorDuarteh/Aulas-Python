import streamlit as st

st.markdown("""
    <style>
            div.stbutton > button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 24px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }
            div.stbutton > button:hover {
                background-color: #45a049;

            }
    </style>
""", unsafe_allow_html=True)

if st.button("Clique aqui"):
    st.write("Você clicou no botão")