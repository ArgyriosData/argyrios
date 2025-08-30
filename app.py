import streamlit as st
import requests
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta

# --- Authenticate with Google Sheets using secrets ---
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_info(st.secrets["google_sheets"], scopes=scope)
client = gspread.authorize(creds)

# --- Connect to your sheet ---
sheet = client.open_by_key("1QUyD9X4jEPkiLt--5oj8QIP7MGv0GGA0Nbr2ZUvXwsw").sheet1

# --- Track session timing ---
now = datetime.now()
date_str = now.strftime("%Y-%m-%d")
time_str = now.strftime("%H:%M:%S")

if "session_start" not in st.session_state:
    st.session_state.session_start = now

session_start = st.session_state.session_start
session_end = now
duration = session_end - session_start
duration_str = str(timedelta(seconds=int(duration.total_seconds())))

# --- Receive location from form submission ---
st.markdown("""
<form id="locationForm" method="POST">
  <input type="hidden" name="region" id="regionInput">
  <input type="hidden" name="country" id="countryInput">
</form>

<script>
fetch("https://ipapi.co/json/")
  .then(response => response.json())
  .then(data => {
    document.getElementById("regionInput").value = data.region;
    document.getElementById("countryInput").value = data.country_name;
    document.getElementById("locationForm").submit();
});
</script>
""", unsafe_allow_html=True)

# --- Read submitted location ---
region = st.session_state.get("region", "Unknown")
country = st.session_state.get("country", "Unknown")

# --- Capture form data on POST ---
if st.request.method == "POST":
    region = st.request.form.get("region", "Unknown")
    country = st.request.form.get("country", "Unknown")
    st.session_state.region = region
    st.session_state.country = country

# --- Log only once per session if location is known ---
if "logged" not in st.session_state and region != "Unknown" and country != "Unknown":
    row = [date_str, time_str, region, country, session_start.strftime("%H:%M:%S"), session_end.strftime("%H:%M:%S"), duration_str]
    sheet.append_row(row)
    st.session_state.logged = True

# --- Your App Content ---
st.set_page_config(page_title="AG", page_icon="📈", layout="centered")
st.title("AG")
st.subheader("Coming Soon, Ignore this till you stop seeing this text :P")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo_AC.jpg", caption="Argyrios — ML Consultant")

st.markdown("""
Welcome to **home**, your partner in intelligent decision-making.
We specialize in delivering tailored machine learning solutions for businesses ready to evolve.
""")

st.markdown("### Services Offered")
st.markdown("""
- 📊 Predictive Modeling  
- 🧹 no  
- 🧠 no  
- 🎓no  
""")

st.markdown("""
📬 Interested in working together?  
[Reach out privately](mailto:georgiadis.argyrios@gmail.com?subject=ML%20Consultancy%20Inquiry)
""")

st.video("https://youtu.be/G0kOefuPZqk?si=Fan_FtZytbZQqM1z")
st.markdown("---")
st.caption("© 2025 Argyrios Georgiadis. All rights reserved.")



# import streamlit as st
# import streamlit_analytics2 as streamlit_analytics

# with streamlit_analytics.track():

#         # Page config
#         st.set_page_config(page_title="AG", page_icon="📈", layout="centered")
        
#         # Header
#         st.title("AG")
#         st.subheader("Coming Soon, Ignore this till you stop seeing this text :P")
        
#         # col1, col2, col3 = st.columns([1, 2, 1])
#         # with col2:
#         #     st.image("logo.jpg", caption="Argyrios — ML Consultant", width=250)
#         col1, col2, col3 = st.columns([1, 2, 1])
#         with col2:
#             st.image("logo_AC.jpg", caption="Argyrios — ML Consultant")
        
#         # About
#         st.markdown("""
#         Welcome to **home**, your partner in intelligent decision-making.
#         We specialize in delivering tailored machine learning solutions for businesses ready to evolve.
#         """)
        
#         # Services
#         st.markdown("### Services Offered")
#         st.markdown("""
#         - 📊 Predictive Modeling  
#         - 🧹 no 
#         - 🧠 no
#         - 🎓no  
#         """)
        
#         # Contact
#         st.markdown("""
#         📬 Interested in working together?  
#         [Reach out privately](mailto:georgiadis.argyrios@gmail.com?subject=ML%20Consultancy%20Inquiry)
#         """)
        
#         st.video("https://youtu.be/G0kOefuPZqk?si=Fan_FtZytbZQqM1z")
        
        
#         # Footer
#         st.markdown("---")
#         st.caption("© 2025 Argyrios Georgiadis. All rights reserved.")
