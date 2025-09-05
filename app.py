import streamlit as st
# from datetime import datetime, timedelta
# import pytz
# import gspread
# from google.oauth2.service_account import Credentials


# --- UI ---
st.title("Argyrios Georgiadis, PhD")
st.subheader("ML Specialist in Gaming & Beyond | Physics PhD | Freelance Projects | Photographer (BA, PgCert)")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo_AC.jpg" )
    # , caption="Argyrios — ML Consultant")

st.markdown("""
## 👤 Profile
- Data Scientist with a PhD in Physics

- 3.5+ years of industry experience in machine learning

- Specialized in behavioral modeling & predictive analytics

- Created models that improved revenue and guided marketing teams in their spending decisions.

- Creative thinker with a background in photography

- Skilled at visualizing and communicating insights clearly

## Education 
- PhD in Physics – University of Surrey (funded by AkzoNobel)  

- BSc in Physics – Aristotle University of Thessaloniki  

- Self-taught in data science, data analytics and machine learning  

- BA in Photography – Open College of the Arts  

- PGCert in Therapeutic Photography – Robert Gordon University

## Relevant Work Experience 
- Fumb Games – London, UK (Remote) 

  Data Scientist, Freelance (Feb 2022 – Present)

- Carma Project – California, USA (Remote)

  Data Scientist, Freelance (May 2022 – Dec 2022) 


""")


st.markdown("""
📬 Interested in working together?  
[Email](mailto:georgiadis.argyrios@gmail.com?subject=ML%20Consultancy%20Inquiry)
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



