import streamlit as st

st.set_page_config(page_title="SafePath", page_icon="🚨")

st.title("SafePath 🚨")
st.subheader("Your Safety Navigation Partner")

st.write("Welcome to SafePath. Stay aware. Stay safe.")

if st.button("Emergency SOS 🚨"):
    st.error("Emergency Alert Sent!")   