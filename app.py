import streamlit as st

st.title("🎉 My First Streamlit App!")
name = st.text_input("What's your name?")
if st.button("Say hello"):
    st.write(f"Hi {name}! 👋 Welcome to Streamlit!")
  
