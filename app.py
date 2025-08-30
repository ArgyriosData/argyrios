import streamlit as st
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(page_title="Location Test", page_icon="🌍", layout="centered")
st.title("🌍 Location Detection Test")

# --- Fetch location from browser using JS ---
location_data = streamlit_js_eval(
    js_expressions="await (await fetch('https://ipapi.co/json/')).json()",
    key="get_location"
)

# --- Display location ---
if location_data:
    region = location_data.get("region", "Unknown")
    country = location_data.get("country_name", "Unknown")
    city = location_data.get("city", "Unknown")
    
    st.success("✅ Location detected!")
    st.markdown(f"**City:** {city}")
    st.markdown(f"**Region:** {region}")
    st.markdown(f"**Country:** {country}")
else:
    st.warning("⏳ Detecting location...")

st.markdown("---")
st.caption("This is a test version. No data is logged.")



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
