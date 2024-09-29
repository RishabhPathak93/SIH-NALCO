# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load the CSV file and specify the correct header row
df = pd.read_csv('Aluminium-Sheet1.csv', header=1)

# Remove any leading/trailing spaces in column names
df.columns = df.columns.str.strip()

# Create a new DataFrame to hold sorted values
sorted_df = pd.DataFrame()

# Sort each column in ascending order
for col in df.columns:
    sorted_df[col] = sorted(df[col])

# Streamlit app layout
st.title("UTS vs Parameters Visualization")

# Sidebar for parameter selection
st.sidebar.header("Parameter Selection")
param_options = sorted_df.columns.tolist()
selected_param = st.sidebar.selectbox("Select a Parameter to Plot", param_options)

# Expander for additional data overview
with st.expander("Data Overview"):
    st.write(df.describe())  # Display summary statistics
    st.write(sorted_df.head())  # Display the first few rows of the sorted DataFrame

# Create a function to plot UTS against the selected parameter
def plot_uts_vs_parameter(parameter):
    plt.figure(figsize=(10, 6))
    plt.plot(sorted_df[parameter], sorted_df['UTS_MPa'], label='UTS (MPa)', color='blue', linewidth=2)
    plt.title(f'Line Chart: UTS vs {parameter}')
    plt.xlabel(parameter)
    plt.ylabel('UTS (MPa)')
    plt.grid(True)
    plt.legend()
    st.pyplot(plt)

# Button to plot the graph
if st.button("Plot Graph"):
    if selected_param != 'UTS_MPa':  # Ensure selected parameter is not UTS
        plot_uts_vs_parameter(selected_param)
    else:
        st.warning("Please select a parameter other than UTS for plotting.")

# Footer
st.markdown("### © Team Capslock | All Rights Reserved")
