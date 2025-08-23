import streamlit as st
st.set_page_config(
    page_title="🌍 Population Dashboard",
    page_icon="📊",
    layout="wide",

)

st.title("🌍 Population Dashboard")
st.markdown("""
Welcome to the <b style="color: yellow">population intelligence dashboard</b>.
This dashboard is designed for **<u>government agencies</u>,<u>NGOS</u>,and <u>researchers</u>** to analyze **population trends** globally or by country.
Use the sidebar to navigate through different modules:
- 📈 **Overview** → See KPIs and population trends  
- ⚖️ **Comparison** → Compare multiple countries  
- 🗺 **Map** → Interactive global population map  
- 🔮 **Forecast** → Predict future population growth  
- 📑 **Raw Data** → Explore and download datasets  
            

""",unsafe_allow_html=True)

