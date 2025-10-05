import streamlit as st

st.title("📝 Mad Libs Story Generator")

noun = st.text_input("Enter a noun:")
verb = st.text_input("Enter a verb:")
place = st.text_input("Enter a place:")

if st.button("Generate Story"):
    story = f"One day, a {noun} decided to {verb} at {place}. It was the best day ever!"
    st.write(story)
