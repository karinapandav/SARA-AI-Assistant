import streamlit as st
from modules.ai_engine import ask_sara

st.set_page_config(
    page_title="SARA",
    layout="wide"
)

st.title("SARA: Smart Adaptive Response Assistant")

st.subheader("Built around you.")
st.subheader("🧠 Teach SARA")

col1, col2 = st.columns(2)

with col1:
    preference_type = st.text_input("Preference Type")
    
with col2:
    preference_value = st.text_input("Preference Value")

if st.button("Save Preference"):

    from modules.memory import add_preference

    add_preference(preference_type, preference_value)

    st.success("SARA learned something new!")

query = st.text_input("Talk to SARA")

if st.button("Send"):

    if query:

        with st.spinner("SARA is thinking..."):

            response = ask_sara(query)

        st.success(response)