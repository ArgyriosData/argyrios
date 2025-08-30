import streamlit as st

# Page config
st.set_page_config(page_title="AG", page_icon="📈", layout="centered")

# Header
st.title("AG")
st.subheader("Coming Soon, Ignore this till you stop seeing this text :P")

# col1, col2, col3 = st.columns([1, 2, 1])
# with col2:
#     st.image("logo.jpg", caption="Argyrios — ML Consultant", width=250)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("argyrios.jpg", caption="Argyrios — ML Consultant")

# About
st.markdown("""
Welcome to **home**, your partner in intelligent decision-making.
We specialize in delivering tailored machine learning solutions for businesses ready to evolve.
""")

# Services
st.markdown("### Services Offered")
st.markdown("""
- 📊 Predictive Modeling  
- 🧹 no 
- 🧠 no
- 🎓no  
""")

# Contact
st.markdown("""
📬 Interested in working together?  
[Reach out privately](mailto:georgiadis.argyrios@gmail.com?subject=ML%20Consultancy%20Inquiry)
""")

st.video("https://youtu.be/G0kOefuPZqk?si=Fan_FtZytbZQqM1z")


# Footer
st.markdown("---")
st.caption("© 2025 Argyrios Georgiadis. All rights reserved.")
