import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Minimal Tracker", page_icon="📊", layout="centered")
st.title("📊 Minimal Visitor Tracker")

# --- Detect if it's you (via query param) ---
is_creator = st.query_params.get("me", "false").lower() == "true"

# --- Track session start ---
if "session_start" not in st.session_state:
    st.session_state.session_start = datetime.now()

# --- Count page views ---
st.session_state.views = st.session_state.get("views", 0) + 1

# --- Calculate duration ---
now = datetime.now()
duration = now - st.session_state.session_start
duration_str = str(timedelta(seconds=int(duration.total_seconds())))

# --- Display tracking info ---
st.markdown(f"**Session started:** {st.session_state.session_start.strftime('%Y-%m-%d %H:%M:%S')}")
st.markdown(f"**Current time:** {now.strftime('%Y-%m-%d %H:%M:%S')}")
st.markdown(f"**Session duration:** {duration_str}")
st.markdown(f"**Page views this session:** {st.session_state.views}")

# --- Mark if it's you ---
if is_creator:
    st.success("👑 This session is marked as yours (Argyrios)")
else:
    st.info("🧍 Visitor session")

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
