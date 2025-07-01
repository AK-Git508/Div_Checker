import streamlit as st
import math

col1,col2,col3, = st.columns([1,2,1])

#   Divison Checker

with col2:
  dividend = int(st.text_input("Enter dividend here: ",value = 5))
  divisor = int(st.text_input("Enter divisor here: ",value = 5))

try:
  st.write (divident/divisor)
except ZeroDivisionError:
  st.write ("Divsor cannot be zero")
  
