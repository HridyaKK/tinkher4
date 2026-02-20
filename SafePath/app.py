import streamlit as st
from datetime import datetime
st.set_page_config(page_title="SafePath", page_icon="🚨", layout="wide")

# HEADER 
st.markdown("""
<h1 style='text-align: center; color: #00C2FF; text-shadow: 0 0 10px rgba(0,194,255,0.6);'>
🛡️ SafePath – Smart Safety Map
</h1>
<p style='text-align: center; font-size:18px; color:#EAF6FF;'>
Real-time safety visualization based on crime, lighting & crowd levels
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# Initialize session state
if "reports" not in st.session_state:
    st.session_state.reports = []

# Sidebar
st.sidebar.title("SafePath 🚨")
page = st.sidebar.radio("Go to", ["Home", "Safety Map", "Report Emergency", "Dashboard"])

    # Home Page
if page == "Home":
    st.subheader("🏠 Home")
    st.subheader("Your Safety Navigation Partner")
    st.write("Welcome to SafePath. Stay aware. Stay safe.")

elif page == "Safety Map":
    st.subheader("🗺️ Safety Map")

    import folium
    from streamlit_folium import st_folium
        

    m = folium.Map(location=[12.9780, 77.6100], zoom_start=12)

    areas = [
        {"name": "MG Road", "lat": 12.9750, "lon": 77.6050,
         "crime": 20, "lighting": 80, "crowd": 70, "night": 0},

        {"name": "Shivaji Nagar", "lat": 12.9850, "lon": 77.5950,
         "crime": 70, "lighting": 40, "crowd": 60, "night": 1},

        {"name": "Indiranagar", "lat": 12.9780, "lon": 77.6400,
         "crime": 40, "lighting": 70, "crowd": 75, "night": 0},
    ]

    # ---------- MARKERS ----------
    for area in areas:
        crime_weight = 0.4
        lighting_weight = 0.2
        crowd_weight = 0.2
        night_penalty = 15 if area["night"] == 1 else 0

        score = (
            (100 - area["crime"]) * crime_weight +
            area["lighting"] * lighting_weight +
            area["crowd"] * crowd_weight
        ) - night_penalty

        score = int(score)

        if score >= 75:
            color = "green"
        elif score >= 50:
            color = "orange"
        else:
            color = "red"

        folium.CircleMarker(
            location=[area["lat"], area["lon"]],
            radius=10,
            color=color,
            fill=True,
            fill_color=color,
            popup=f"{area['name']} - Safety Score: {score}"
        ).add_to(m)

   

    # ---------- LEGEND ----------
    
    legend_html = """
    <div style="
    position: absolute;
    bottom: 50px;
    left: 50px;
    width: 200px;
    background-color: white;
    border: 2px solid grey;
    z-index: 9999;
    font-size: 14px;
    padding: 10px;
    border-radius: 8px;
    box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
    color: black;
    ">
    <b>Safety Legend</b><br>
    <span style="color:green;">●</span> Safe (75+)<br>
    <span style="color:orange;">●</span> Moderate (50–74)<br>
    <span style="color:red;">●</span> Risky (&lt;50)
    </div>
    """

    m.get_root().html.add_child(folium.Element(legend_html))
    st_folium(m, width=700, height=500)
# Report Emergency Page
elif page == "Report Emergency":
    st.subheader("🚨 Report Emergency")

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
    st.subheader("📊 Safety Dashboard")
    if len(st.session_state.reports) > 0:
        for i, report in enumerate(st.session_state.reports, start=1):
            st.write(f"### Report {i}")
            st.write("🕒 Time:", report["time"])
            st.write("📍 Location:", report["location"])
            st.write("📝 Issue:", report["issue"])
            st.markdown("---")
    else:
        st.info("No emergency reports yet.")