import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

size = st.slider("Sample size", 200, 1500)

arr = np.random.normal(1, 1, size=size)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
