import streamlit as st

st.write("Hello, *World!* :sunglasses:")
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.header("_Streamlit_ is :blue[cool] :sunglasses:")
col1.metric("Temperature", "70 °F", "1.2 °F")
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
