import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

rows = np.random.randn(1,1)
all_rows = rows 

'Growing Line Chart: '
chart = st.line_chart(rows)

for i in range(1, 100):
    new_rows = rows[0] + np.random.randn(1,1)
    all_rows = np.vstack([all_rows, new_rows])
    chart.line_chart(all_rows)
    rows = new_rows
    time.sleep(0.05)

    values = np.random.rand(10)
    'matplotlib Line chart: '
    fig, ax = plt.subplots()
    ax.plot(values)
    st.pyplot(fig)