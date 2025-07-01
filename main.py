import streamlit as st

#   Divison Checker

dividend = int(input("Enter dividend here: "))
divisor = int(input("Enter divisor here: "))

try:
  print (divident/divisor)
except ZeroDivisionError
  print ("Divsor cannot be zero")
