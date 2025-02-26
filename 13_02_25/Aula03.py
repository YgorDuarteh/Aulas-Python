import streamlit as st

st.title("Calculadora de salario liquido")

valor_inss = 0

salario_bruto = st.number_input("Digite o salario bruto:", format="%.2f")
turno = st.selectbox("Selecione o turno de trabalho:", ["Diurno", "Noturno"])

if turno == "Diurno":
    gratificacao = 0
else:
    gratificacao = 0.20

if st.button("Calcular salario liquido"):
    if salario_bruto <= 1518.00:
        valor_inss = salario_bruto * 0.075
    elif salario_bruto <= 2793.88:
        valor_inss = salario_bruto * 0.09 - 22.77
    elif salario_bruto <= 4190.83:
        valor_inss = salario_bruto * 0.12 - 106.60
    elif salario_bruto <= 8157.41:
        valor_inss = salario_bruto * 0.14 - 190.42
    else:
        valor_inss = 8157.41 * 0.14 - 190.42

base_calculo_irrf = salario_bruto - valor_inss
if base_calculo_irrf <= 2259.20:
    valor_irrf = 0.0
elif base_calculo_irrf <= 2828.65:
    valor_irrf = base_calculo_irrf * 0.075 - 169.44
elif base_calculo_irrf <= 3751.05:
    valor_irrf = base_calculo_irrf * 0.15 - 381.44
elif base_calculo_irrf <= 4664.68:
    valor_irrf = base_calculo_irrf * 0.225 - 662.77
else:
    valor_irrf = base_calculo_irrf * 0,275 - 896.00

salario_liquido = salario_bruto - valor_inss - valor_irrf + (salario_bruto * gratificacao)

st.write(f"**Salario Bruto:** R$ {salario_bruto:.2f}")
st.write(f"**Desconto INSS:** R$ {valor_inss:.2f}")
st.write(f"**Desconto IRRF:** R$ {valor_irrf:.2f}")
st.write(f"**Gratificação:** R$ {salario_bruto * gratificacao:.2f}")
st.write(f"**Salario Liquido:** R$ {salario_liquido:.2f}")