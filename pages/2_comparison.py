import streamlit as st
import pandas as pd
import plotly.express as px
st.title("📊 Country Comparison")
@st.cache_data
def load_data():
    return   pd.read_csv(r"C:\Users\USER\Population_updated")
    
df= load_data()

countries= st.sidebar.multiselect("Select Countries to compare",df["Country Name"].unique(), default=["Rwanda","Uganda","Tanzania"])
st.info("population comparison between different countries")

filtered_df= df[df["Country Name"].isin(countries)]

if "selected_year" not in st.session_state:
    st.session_state.selected_year = 2024

projection_year = st.sidebar.slider("Select projection year" ,min_value=df["Year"].min(), max_value=df["Year"].max(), value=st.session_state.selected_year)
st.session_state.selected_year = projection_year

cols= st.columns(len(countries))

for i , country in enumerate(countries):
    country_df= filtered_df[filtered_df["Country Name"] == country]
    
    last_year_population = country_df[country_df["Year"] == projection_year]["population"].values[0]

    with cols[i]:
        st.metric(f"Population of {country} in {projection_year}", f"{int(last_year_population):,}")

        df_projection=filtered_df[filtered_df["Year"] == projection_year]
        st.subheader(f"{country} Population insights in {projection_year}")
        fig=px.bar(df_projection,x="Country Name", y="population", title=f" Population comparison in {projection_year}", text="population")
        fig.update_traces(texttemplate='%{text:,}', textposition="outside")
st.plotly_chart(fig, use_container_width=True)