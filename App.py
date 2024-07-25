import streamlit as st
import pickle as pk

model = open("model.pkl", "rb")
model = pk.load(model)

st.write("""# Demand Forcasting App""")
st.write("""Demand forecasting in the organic food industry is a crucial aspect of business planning, 
         as it involves predicting consumer preferences and market trends for organic products.
         Accurate forecasting helps organic food companies optimize production, reduce waste, 
         and ensure they meet the growing demand for environmentally-friendly and healthy food options.
         """)
slider = st.slider("Window Period[Weeks]", min_value=52, max_value=600)
st.write(f"{slider} Weeks")
st.line_chart(data=model.forecast(slider))