import streamlit as st
import pandas as pd
import plotly.express as px


st.write('# Kenya - Food Prices 2006 - 2022')  #st.title('Kenya - Food Prices')
st.markdown('''
This is a dashboard showing the *average prices* of different types of : Foods items in Kenya:  
Data source: [Humdata](https://data.humdata.org/dataset/wfp-food-prices-for-kenya)
''')
#st.header('Summary statistics')
#st.header('Line chart by Regions')


st.header('Summary statistics')
food = pd.read_csv('wfp_food_prices_ken.csv')
food_stats = food.groupby('category')['avg_price'].mean()
st.dataframe(food_stats)
# wfp_food_prices_ken


st.header('Line chart by Counties/Regions')
line_fig = px.line(food[food['market'] == 'Nairobi'],
                   x='date', y='avg_price',
                   color='pricetype',
                   title='Prices Prices in Nairobi')
st.plotly_chart(line_fig)


selected_geography = st.selectbox(label='Region', options=food['market'].unique())
#submitted = st.form_submit_button('Submit')
submitted =  st.button('Submit')

if submitted:
    filtered_food = food[food['market'] == selected_geography]
    
    line_fig = px.line(filtered_food,
                       x='date', y='avg_price',
                       color='pricetype',
                       title=f'Avg Food Prices in K.Sh. in {selected_geography}')
    st.plotly_chart(line_fig)
    
    with st.sidebar:
        st.subheader('About')
        st.markdown('This dashboard is made by George Ndede using **Streamlit library**')
        st.markdown('For those who want to Learn Data Science with Visualization')
        st.markdown('Using Humadata on the Food Prices in Kenya')