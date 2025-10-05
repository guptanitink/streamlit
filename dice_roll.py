import streamlit as st
import random

st.title("🎲 Dice Roller")

if st.button("Roll the dice!"):
    roll = random.randint(1, 6)
    st.write(f"You rolled a **{roll}**!")
