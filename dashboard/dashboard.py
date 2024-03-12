import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

#membuka dataframe
year_df = pd.read_csv("dashboard\years.csv")
month_df = pd.read_csv("dashboard\month.csv")

st.title("ini dashboard")

