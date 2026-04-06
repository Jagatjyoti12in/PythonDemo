
# 1. import  streamlit as st

import streamlit as st
#2. Add a Title to your app
st.title("Welcome to the Square Calculator App")
#3. Add a header, subheader, text, markdown, latex, code and write
st.write("Welcome ! This app calculates the square of a number")
st.header("Select the Number to Square")
st.subheader("This is a subheader")
number = st.number_input("Enter a number", value=0)
#number =  st.slider("Select a number", min_value=0, max_value=100, value=0)
st.sidebar.header("Sidebar Header")
st.sidebar.subheader("Sidebar Subheader")
username = st.sidebar.text_input("Enter your username")

square = number ** 2
st.write(f"The square of {number} is {square}")

