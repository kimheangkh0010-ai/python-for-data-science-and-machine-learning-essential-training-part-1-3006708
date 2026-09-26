import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

animals = ['cat', 'cow', 'dog', 'goat']
height = [30, 150, 80, 60]
weight = [10, 400, 30, 40]

fig, ax = plt.subplots()

x = np.arange(len(height))
width =0.40

ax.bar(x-0.2, height, width, color='red')
ax.bar(x+0.2, weight, width, color='orange')
ax.legend(['height', 'weight'])
ax.set_xticks(x)
ax.set_xticklabels(animals)

st.pyplot(fig)

explode = [0.2, 0.1, 0.1, 0.1]
plot_pie, ax = plt.subplots()
ax.pie(height, explode=explode, labels=animals, autopct='%1.1f%%', shadow=True)
ax.axis('equal')

st.pyplot(plot_pie)