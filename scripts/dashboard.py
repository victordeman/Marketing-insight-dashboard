import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('DHL Campaign Analytics Dashboard')
metrics = pd.read_csv('data/campaign_metrics.csv')

# Plot email open rates by region
st.subheader('Email Open Rates by Region')
fig, ax = plt.subplots()
metrics.groupby('region')['email_open'].mean().plot(kind='bar', ax=ax)
st.pyplot(fig)

# Plot LinkedIn engagement
st.subheader('LinkedIn Engagement Trends')
engagement = pd.read_csv('data/linkedin_engagement.csv')
st.line_chart(engagement[['likes', 'comments']])
