import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Title of the app
st.title("My Streamlit App")

# Add a description
st.write("This is a sample app similar to https://wccnnrms.streamlit.app/.")

# Example: Load a dataset
data = pd.DataFrame({
    'x': np.arange(100),
    'y': np.random.randn(100)
})

# Display the data
st.write("Sample Data:")
st.write(data)

# Example: Create a Plotly chart
fig = px.line(data, x='x', y='y', title="Sample Line Chart")
st.plotly_chart(fig)

# Add more features as needed