import streamlit as st
import pandas as pd

# Load data from Excel file
file_path = "categorized_stocks_data_industry_standards.xlsx"
df = pd.read_excel(file_path)

# Sidebar for user inputs
st.sidebar.header("PredictRAm Stock Filter")
st.sidebar.header("Filter Options")

# Dropdown for Industry Sector
selected_sector = st.sidebar.selectbox("Select Industry Sector", df['Industry_Sector'].unique())

# Slider for Beta
beta_range = st.sidebar.slider("Select Beta Range", -1.5, 2.507, (-1.5, 2.507))

# Slider for P/E Ratio
pe_ratio_range = st.sidebar.slider("Select P/E Ratio Range", 0, 5000, (0, 5000))

# Slider for P/B Ratio
pb_ratio_range = st.sidebar.slider("Select P/B Ratio Range", 0, 1080, (0, 1080))

# Slider for EPS
eps_range = st.sidebar.slider("Select EPS Range", -464.16, 3982.57, (-464.16, 3982.57))

# Slider for Dividend Yield
dividend_yield_range = st.sidebar.slider("Select Dividend Yield Range", 0.0, 0.271, (0.0, 0.0))

# Apply filters to the dataframe
filtered_df = df[(df['Industry_Sector'] == selected_sector) &
                 (df['Beta'] >= beta_range[0]) & (df['Beta'] <= beta_range[1]) &
                 (df['P/E_Ratio'] >= pe_ratio_range[0]) & (df['P/E_Ratio'] <= pe_ratio_range[1]) &
                 (df['P/B_Ratio'] >= pb_ratio_range[0]) & (df['P/B_Ratio'] <= pb_ratio_range[1]) &
                 (df['EPS'] >= eps_range[0]) & (df['EPS'] <= eps_range[1]) &
                 (df['Dividend_Yield'] >= dividend_yield_range[0]) & (df['Dividend_Yield'] <= dividend_yield_range[1])]

# Display results
st.header("Filtered Results")
st.write(filtered_df)
