from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # Get visitor's IP address
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    # Fetch location from IP
    try:
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        data = response.json()
        city = data.get("city", "Unknown")
        region = data.get("region", "Unknown")
        country = data.get("country_name", "Unknown")
    except:
        city, region, country = "Unknown", "Unknown", "Unknown"

    # Display result
    html = f"""
    <h1>🌍 Location Detection</h1>
    <p><strong>IP:</strong> {ip}</p>
    <p><strong>City:</strong> {city}</p>
    <p><strong>Region:</strong> {region}</p>
    <p><strong>Country:</strong> {country}</p>
    <hr>
    <p>This is a test version. No data is logged.</p>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)


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
