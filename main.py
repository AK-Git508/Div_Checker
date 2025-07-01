import streamlit as st
import math

col1,col2,col3, = st.columns([1,2,1])

#   Divison Checker

with col2:
  dividend = int(st.text_input("Enter dividend here: ",value))
  divisor = int(st.text_input("Enter divisor here: ",value))

try:
  st.write (divident/divisor)
except ZeroDivisionError:
  st.write ("Divsor cannot be zero")
  
