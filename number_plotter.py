import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Favorite Numbers Plotter")

points = st.slider("How many points?", 5, 50, 10)
x = np.linspace(0, 10, points)
y = np.sin(x)

data = pd.DataFrame({"x": x, "y": y})
st.line_chart(data.set_index("x"))
