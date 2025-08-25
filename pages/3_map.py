import streamlit as st
import pandas as pd
import plotly.express as px 

st.title(" 🗺️ Global population Map")
@st.cache_data
def load_data():
    return pd.read_csv("data1/merged_data_withcoordinates.csv")

data_with_coordinates = load_data()

if "selected_year" not in st.session_state:
    st.session_state.selected_year = 2025

years = pd.to_numeric(data_with_coordinates["Year"], errors="coerce")  
years = years.dropna()

projection_year = st.sidebar.slider("Select Year",
    min_value=int(years.min()),
    max_value=int(years.max()),
    value=int(st.session_state.selected_year)
)

st.session_state.selected_year = projection_year

filtered_data = data_with_coordinates[data_with_coordinates["Year"] == projection_year]
filtered_data["population"] = pd.to_numeric(filtered_data["population"], errors='coerce')

filtered_data= filtered_data.dropna(subset=["population"])



st.subheader(f"Population Map in {projection_year}")
st.info("Hover over the map to see the country name and population")
st.info("choose between choropleth map and scatter map")
tab1,tab2 = st.tabs([" cholopleth Map","Scatter Map"])

with tab1:
     @st.fragment
     def print_map():
         fig1 = px.choropleth(filtered_data, locations="Country Name", 
                              locationmode="country names", 
                              color="population", hover_name="Country Name",
                                color_continuous_scale="viridis", 
                                title=f"population in {projection_year}")
         st.plotly_chart(fig1, use_container_width=False)
        
         
         return fig1
     
colored_map = print_map()
     
with tab2:
    @st.fragment
    def print_map2():
        fig2 = px.scatter_geo(filtered_data, lat="latitude", lon="longitude", color="Country Name", size="population", hover_name="Country Name", title=f"population in {projection_year}",projection="natural earth")
        st.plotly_chart(fig2, use_container_width=False)
        return fig2
scatter_map = print_map2()


    