import streamlit as st
from datetime import datetime
st.set_page_config(page_title="SafePath", page_icon="🚨")

# Initialize session state
if "reports" not in st.session_state:
    st.session_state.reports = []

# Sidebar
st.sidebar.title("SafePath 🚨")
page = st.sidebar.radio("Go to", ["Home", "Safety Map", "Report Emergency", "Dashboard"])

# Home Page
if page == "Home":
    st.title("SafePath 🚨")
    st.subheader("Your Safety Navigation Partner")
    st.write("Welcome to SafePath. Stay aware. Stay safe.")

elif page == "Safety Map":
    st.title("🗺️ Safety Route Map")

    import folium
    from streamlit_folium import st_folium

    # Center map (example: Bangalore)
    m = folium.Map(location=[12.9716, 77.5946], zoom_start=13)

    # Dummy safety data
    areas = [
        {"name": "MG Road", "lat": 12.9750, "lon": 77.6050, "score": 85},
        {"name": "Shivaji Nagar", "lat": 12.9850, "lon": 77.5950, "score": 45},
        {"name": "Indiranagar", "lat": 12.9780, "lon": 77.6400, "score": 65},
    ]

    for area in areas:
        score = area["score"]

        if score >= 75:
            color = "green"
        elif score >= 50:
            color = "orange"
        else:
            color = "red"

        folium.CircleMarker(
            location=[area["lat"], area["lon"]],
            radius=10,
            popup=f"{area['name']} - Safety Score: {score}",
            color=color,
            fill=True,
            fill_color=color,
        ).add_to(m)

    st_folium(m, width=700, height=500)
    
# Report Emergency Page
elif page == "Report Emergency":
    st.title("🚨 Report Emergency")

    location = st.text_input("Enter your current location")
    issue = st.text_area("Describe the emergency")

    if st.button("Send Alert"):
        if not location or not issue:
            st.error("Please fill in all fields before sending alert.")
        else:
            report = {
    "location": location,
    "issue": issue,
    "time": datetime.now().strftime("%d %b %Y - %I:%M %p")
}
            st.session_state.reports.append(report)
            st.success("Emergency Alert Sent Successfully!")

# Dashboard Page
elif page == "Dashboard":
    st.title("📊 Safety Dashboard")

    if len(st.session_state.reports) > 0:
        for i, report in enumerate(st.session_state.reports, start=1):
            st.write(f"### Report {i}")
            st.write("🕒 Time:", report["time"])
            st.write("📍 Location:", report["location"])
            st.write("📝 Issue:", report["issue"])
            st.markdown("---")
    else:
        st.info("No emergency reports yet.")