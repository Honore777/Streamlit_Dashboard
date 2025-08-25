import streamlit as st
import pandas as pd
import plotly.express as px
@st.cache_data
def load_data():
    return   pd.read_csv(r"C:\Users\USER\Population_updated.csv")
    
df= load_data()

st.sidebar.header("Filters")

default_country="Rwanda"
default_index=list(df["Country Name"].unique()).index(default_country)

country= st.sidebar.selectbox("Select a country",df["Country Name"].unique(),index=default_index)
if "projection_year" not in st.session_state:
    st.session_state.projection_year = 2050
projection_year = st.sidebar.slider("Select projection year" ,min_value=df["Year"].min(), max_value=df["Year"].max(), value=st.session_state.projection_year, step=1)
st.session_state.projection_year = projection_year

if "current_year" not in st.session_state:
    st.session_state.current_year = 2025



filtered_country_dataframe = df[df["Country Name"] == country]
current_year = st.sidebar.slider("Select current year" , df["Year"].min(), df["Year"].max(), value=st.session_state.current_year)
st.session_state.current_year = current_year




last_year_population= filtered_country_dataframe[filtered_country_dataframe["Year"] == current_year]["population"].values[0]

if projection_year in filtered_country_dataframe["Year"].values:
    projection_pop= filtered_country_dataframe[filtered_country_dataframe["Year"] == projection_year]["population"].values[0]
else:
    projection_pop=None
    

st.subheader(f"{country} Population insights")
col1,col2,col3= st.columns(3)
with col1:
    st.metric(f"Population in {current_year}", f"{int(last_year_population):,}")

with col2:
    if projection_pop:
        st.metric(f"Population in {projection_year}", f"{int(projection_pop):,}")

with col3:
    if projection_pop:
        growth = int(projection_pop) - int(last_year_population)
        st.metric(f"Growth ({current_year} → {projection_year})", f"{growth:,}")

@st.fragment
def plot_population_trend():
    fig= px.line(filtered_country_dataframe, x="Year", y="population", title=f"{country} Population over time")
    st.plotly_chart(fig, use_container_width=True)

plot_population_trend()
with st.expander("See Raw Data"):
     st.dataframe(filtered_country_dataframe)
        



    