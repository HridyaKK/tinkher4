import streamlit as st

st.set_page_config(page_title="SafePath", page_icon="🚨")

# Sidebar Navigation
st.sidebar.title("SafePath 🚨")
page = st.sidebar.radio("Go to", ["Home", "Report Emergency", "Dashboard"])

# Home Page
if page == "Home":
    st.title("SafePath 🚨")
    st.subheader("Your Safety Navigation Partner")
    st.write("Welcome to SafePath. Stay aware. Stay safe.")

# Report Emergency Page
elif page == "Report Emergency":
    st.title("🚨 Report Emergency")

    location = st.text_input("Enter your current location")
    issue = st.text_area("Describe the emergency")

    if st.button("Send Alert"):
        if not location or not issue:
            st.error("Please fill in all fields before sending alert.")
        else:
            st.success("Emergency Alert Sent Successfully!")
            st.write("📍 Location:", location)
            st.write("📝 Issue:", issue)

# Dashboard Page
elif page == "Dashboard":
    st.title("📊 Safety Dashboard")
    st.info("Dashboard data will appear here.")