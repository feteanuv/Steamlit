import streamlit as st
import pandas


data = {
    'Series_1':[1, 2, 3, 4, 6],
    'Series_2':[10, 20, 30, 50, 70]
}

df = pandas.DataFrame(data)

st.title('My Fist Streamlit App')
st.subheader('Introducing Streamlit in Automate Everything with Python')
st.write('''This is our first Web App.

Enjoy it!
''')

st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider = st.slider('Celsius')
st.write(myslider, '°C | in Fahrenheit is', myslider * 9/5 + 32)

#  to run app, we have to type in terminal 'streamlit run name.py'