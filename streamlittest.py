import streamlit as st
import pandas as pd
import numpy as np

# Ensure wide mode is enabled
st.set_page_config(layout="wide")

# CSS to clean up spacing
st.markdown("""
    <style>
    .block-container {
        padding-top: 2rem;
    }
    /* Makes the chart and list align better at the top of their columns */
    .stPlotlyChart, .stTable, .stMarkdown {
        margin-top: 0px;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. Top Section (Now fills the entire top)
st.title("Hello! [12:00]")
st.subheader("Safe")
st.write(""" """)
st.write(""" """)
st.write(""" """)
st.write(""" """)

# This creates the horizontal line separating top from bottom
st.divider()

# 2. Bottom Section (50/50 split)
# Using [1, 1] ensures they take up exactly half the frame each
left_col, right_col = st.columns([1, 1])

with left_col:
    st.write("### Trends")
    chart_data = pd.DataFrame(np.random.randn(20, 1), columns=['Value'])
    st.line_chart(chart_data)

with right_col:
    st.write("### Notes")
    # Limiting to exactly 5 units as requested
    for i in range(1, 6):
        st.write(f"{i}. System Log Entry {chr(64+i)}")
    
    # Optional: fill the rest of the frame with empty space if needed
    # for _ in range(10): st.write("")
