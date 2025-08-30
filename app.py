import streamlit as st
import streamlit.components.v1 as components

# 🔹 Replace with your GA4 Measurement ID
GA_TRACKING_ID = "G-RZZMRJV9JP"

GA_JS = f"""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_TRACKING_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_TRACKING_ID}');

  // 🔹 Send a custom test event when the app loads
  gtag('event', 'streamlit_test_event', {{
    'event_category': 'debug',
    'event_label': 'GA script loaded successfully',
    'value': 1
  }});
</script>
"""

# Inject GA tracking script
components.html(GA_JS, height=0, width=0)

# Minimal app UI
st.title("GA4 Test App")
st.write("👋 Hello! If GA is working, you should see a `streamlit_test_event` in DebugView.")



# import streamlit as st
# import streamlit.components.v1 as components

# GA_TRACKING_ID = "G-RZZMRJV9JP"  # 👈 your GA measurement ID

# GA_JS = f"""
# <!-- Google tag (gtag.js) -->
# <script async src="https://www.googletagmanager.com/gtag/js?id={GA_TRACKING_ID}"></script>
# <script>
#   window.dataLayer = window.dataLayer || [];
#   function gtag(){{dataLayer.push(arguments);}}
#   gtag('js', new Date());
#   gtag('config', '{GA_TRACKING_ID}');
# </script>
# """

# # This makes sure the script is injected and executed
# components.html(GA_JS, height=0, width=0)


# # Page config
# st.set_page_config(page_title="AG", page_icon="📈", layout="centered")

# # Header
# st.title("AG")
# st.subheader("Coming Soon, Ignore this till you stop seeing this text :P")

# # col1, col2, col3 = st.columns([1, 2, 1])
# # with col2:
# #     st.image("logo.jpg", caption="Argyrios — ML Consultant", width=250)
# col1, col2, col3 = st.columns([1, 2, 1])
# with col2:
#     st.image("logo_AC.jpg", caption="Argyrios — ML Consultant")

# # About
# st.markdown("""
# Welcome to **home**, your partner in intelligent decision-making.
# We specialize in delivering tailored machine learning solutions for businesses ready to evolve.
# """)

# # Services
# st.markdown("### Services Offered")
# st.markdown("""
# - 📊 Predictive Modeling  
# - 🧹 no 
# - 🧠 no
# - 🎓no  
# """)

# # Contact
# st.markdown("""
# 📬 Interested in working together?  
# [Reach out privately](mailto:georgiadis.argyrios@gmail.com?subject=ML%20Consultancy%20Inquiry)
# """)

# st.video("https://youtu.be/G0kOefuPZqk?si=Fan_FtZytbZQqM1z")


# # Footer
# st.markdown("---")
# st.caption("© 2025 Argyrios Georgiadis. All rights reserved.")
