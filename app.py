import streamlit as st
from datetime import datetime, timedelta
import pytz
import gspread
from google.oauth2.service_account import Credentials

# # --- Timezone ---
# local_tz = pytz.timezone("Europe/Athens")

# # --- Page config ---
# st.set_page_config(page_title="AG", page_icon="📈", layout="centered")

# # --- Track session start ---
# if "session_start" not in st.session_state:
#     st.session_state.session_start = datetime.now(pytz.utc)

# # --- Count page views ---
# st.session_state.views = st.session_state.get("views", 0) + 1

# # --- Calculate duration ---
# now_utc = datetime.now(pytz.utc)
# session_start_local = st.session_state.session_start.astimezone(local_tz)
# now_local = now_utc.astimezone(local_tz)
# duration = now_local - session_start_local
# duration_str = str(timedelta(seconds=int(duration.total_seconds())))

# # --- Log to Google Sheets (silent fail) ---
# def log_to_sheet():
#     try:
#         creds = Credentials.from_service_account_info(
#             st.secrets["google_sheets"],
#             scopes=["https://www.googleapis.com/auth/spreadsheets"]
#         )
#         client = gspread.authorize(creds)
#         sheet = client.open_by_key("1QUyD9X4jEPkiLt--5oj8QIP7MGv0GGA0Nbr2ZUvXwsw").worksheet("Sheet1")
#         sheet.append_row([
#             now_local.strftime('%Y-%m-%d %H:%M:%S'),
#             duration_str,
#             st.session_state.views
#         ])
#     except:
#         pass  # Silently ignore any logging errors

# log_to_sheet()

# --- UI ---
st.title("Argyrios Georgiadis, PhD")
st.subheader("ML Specialist in Gaming & Beyond | Physics PhD | Freelance Projects | Photographer (BA, PgCert)")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo_AC.jpg", caption="Argyrios — ML Consultant")

st.markdown("""
👤 Profile
Data Scientist with a PhD in Physics

3.5+ years of industry experience in machine learning

Specialized in behavioral modeling & predictive analytics

Proven impact in gaming: models that boost marketing and revenue

Creative thinker with a background in photography

Skilled at visualizing and communicating insights clearly
""")

st.markdown("### Services Offered")
st.markdown("""
- 📊 Predictive Modeling  
- 🧹 no  
- 🧠 no  
- 🎓 no  
""")

st.markdown("""
📬 Interested in working together?  
[Reach out privately](mailto:georgiadis.argyrios@gmail.com?subject=ML%20Consultancy%20Inquiry)
""")

with open("CV.pdf", "rb") as f:
    pdf_bytes = f.read()

st.download_button(
    label="Download CV",
    data=pdf_bytes,
    file_name="CV.pdf",
    mime="application/pdf"
)

st.video("https://youtu.be/j_YugmZPIfk")

st.markdown("---")
st.caption("© 2025 Argyrios Georgiadis. All rights reserved.")




# import streamlit as st
# from datetime import datetime, timedelta
# import pytz
# import gspread
# from google.oauth2.service_account import Credentials
# import random
# import string

# # --- Timezone ---
# local_tz = pytz.timezone("Europe/Athens")

# # --- Page config ---
# st.set_page_config(page_title="AG", page_icon="📈", layout="centered")

# import streamlit.components.v1 as components

# components.html("""
# <script data-goatcounter="https://argyrios.goatcounter.com/count"
#         async src="//gc.zgo.at/count.js"></script>
# """, height=0)


# # --- Detect if it's you ---
# query = st.query_params
# me_raw = query.get("me", "false")
# me_value = me_raw[0] if isinstance(me_raw, list) else me_raw
# is_creator = me_value.strip().lower() == "true"

# # --- Generate anonymous ID ---
# if "anon_id" not in st.session_state:
#     st.session_state.anon_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
# anon_id = st.session_state.anon_id

# # --- Track session start ---
# if "session_start" not in st.session_state:
#     st.session_state.session_start = datetime.now(pytz.utc)

# # --- Count page views ---
# st.session_state.views = st.session_state.get("views", 0) + 1

# # --- Calculate duration ---
# now_utc = datetime.now(pytz.utc)
# session_start_local = st.session_state.session_start.astimezone(local_tz)
# now_local = now_utc.astimezone(local_tz)
# duration = now_local - session_start_local
# duration_str = str(timedelta(seconds=int(duration.total_seconds())))

# # --- Log to Google Sheets (silent fail) ---
# def log_to_sheet():
#     try:
#         creds = Credentials.from_service_account_info(
#             st.secrets["google_sheets"],
#             scopes=["https://www.googleapis.com/auth/spreadsheets"]
#         )
#         client = gspread.authorize(creds)
#         sheet = client.open_by_key("1QUyD9X4jEPkiLt--5oj8QIP7MGv0GGA0Nbr2ZUvXwsw").worksheet("Sheet1")
#         sheet.append_row([
#             now_local.strftime('%Y-%m-%d %H:%M:%S'),
#             duration_str,
#             st.session_state.views,
#             str(is_creator),
#             anon_id
#         ])
#     except:
#         pass  # Silently ignore any logging errors

# log_to_sheet()

# # --- UI ---
# st.title("AG")
# st.subheader("Coming Soon, Ignore this till you stop seeing this text :P")

# col1, col2, col3 = st.columns([1, 2, 1])
# with col2:
#     st.image("logo_AC.jpg", caption="Argyrios — ML Consultant")

# st.markdown("""
# Welcome to **home**, your partner in intelligent decision-making.  
# We specialize in delivering tailored machine learning solutions for businesses ready to evolve.
# """)

# st.markdown("### Services Offered")
# st.markdown("""
# - 📊 Predictive Modeling  
# - 🧹 no  
# - 🧠 no  
# - 🎓 no  
# """)

# st.markdown("""
# 📬 Interested in working together?  
# [Reach out privately](mailto:georgiadis.argyrios@gmail.com?subject=ML%20Consultancy%20Inquiry)
# """)

# st.video("https://youtu.be/G0kOefuPZqk?si=Fan_FtZytbZQqM1z")

# st.markdown("---")
# st.caption("© 2025 Argyrios Georgiadis. All rights reserved.")


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
