import streamlit as st
import pandas as pd





st.title("Welcome!")
st.title("MSBA 325 - Assignment 3")
st.title("Dr. Fouad Zablith")
st.title("22-9-2022")
st.title("By Hassan Hodroj")


st.markdown("<h1 style='text-align: left; color: red;font-size:7'>House Rent</h1>", unsafe_allow_html=True)


data=pd.read_csv("/Users/hassan/Desktop/AUB/MSBA 325/House_Rent_Dataset.csv")
import plotly.express as px



if st.checkbox("Show Center Information data"):
    st.subheader("Center Information data")
    st.write(data.head())


fig=px.scatter(data, x= "Rent", y= "Size", color= "Size", title="Relation between Size and Rent")
st.plotly_chart(fig,use_container_width=False)




fig12=px.scatter_3d(data, x= "Rent", y= "Size", z="BHK", color= "Size", title="Relation between Size and Rent 3D")
st.plotly_chart(fig12,use_container_width=False)

dfg=data.groupby(['Area Type']).count()
fig1=px.bar(dfg, x=dfg.index,y=[2,2298,2446], title='Area Type by Count', 
           labels=dict(y="Count"))
st.plotly_chart(fig1,use_container_width=False)

fig2=px.box(data, y= "BHK", color= "Area Type", title="BHK Distribution by Area Type")
st.plotly_chart(fig2,use_container_width=False)

fig3=px.pie(data, values= "Floor", names= "Floor", title="Number of Floors")
st.plotly_chart(fig3,use_container_width=False)

fig4=px.histogram(data, x= "Rent", color= "Furnishing Status", title="Distribution of Rent by Furnishing Status")
st.plotly_chart(fig4,use_container_width=False)

st.sidebar.title("Introduction")
st.sidebar.title("Relation between Size and Rent")
st.sidebar.title("Relation between Size and Rent 3D")
st.sidebar.title("Area Type by Count")
st.sidebar.title("BHK Distribution by Area Type")
st.sidebar.title("Number of Floors")
st.sidebar.title("Distribution of Rent by Furnishing Status")
option = st.selectbox(
    'How would you like to receive the data?',
    ('Email', 'Mobile phone'))

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(data)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)

st.success('You Reached The End! Thanks for reading.')

st.snow()



st.title("By Hassan Hodroj")