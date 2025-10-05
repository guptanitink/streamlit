import streamlit as st

st.title("🎨 Mood Color Picker")

mood = st.radio("How are you feeling today?", ["Happy 😊", "Calm 😌", "Energetic ⚡", "Sleepy 😴"])
color = st.color_picker("Pick a color that matches your mood:")

st.write(f"Your mood is {mood} and your color is {color}!")
st.markdown(f"<div style='background-color:{color};height:100px;border-radius:10px'></div>", unsafe_allow_html=True)
