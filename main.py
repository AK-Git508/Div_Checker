import streamlit as st

col1, col2, col3 = st.columns([1, 2, 1]) 

with col2:
    st.title("Div Checker")
    dividend_input = st.text_input("Enter your dividend here:", value="5")
    divisor_input = st.text_input("Enter your divisor here:", value="5")

try:
    dividend = int(dividend_input)
    divisor = int(divisor_input)
    result = dividend / divisor
    st.write(f"Result: {result}")
except ZeroDivisionError:
    st.write("❌ The divisor cannot be zero!")
except ValueError:
    st.write("❌ Make sure to enter valid numbers for both dividend and divisor!")

st.header("Description")
st.write("A simple web application created using python libraries such as Streamlit that calculates the result of a division expression.")

for i in range(2):
    st.write("")

st.write("Developed by Aariz Khan and Kabir Tiwari")
