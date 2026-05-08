import streamlit as st
from modules.ai_engine import ask_sara

st.set_page_config(
    page_title="SARA",
    layout="wide"
)

st.title("SARA: Smart Adaptive Response Assistant")

st.subheader("Built around you.")

query = st.text_input("Talk to SARA")

if st.button("Send"):

    if query:

        with st.spinner("SARA is thinking..."):

            response = ask_sara(query)

        st.success(response)