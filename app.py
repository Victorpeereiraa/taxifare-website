import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
date = st.date_input("Input the date",  value=datetime.date(2014, 7, 6))
time = st.time_input("Input the time", value=datetime.time(19, 18, 0))
long = st.number_input("Input the longitude", value = -73.950655, step = 0.000001, format="%0.6f")
lat = st.number_input("Input the latitude", value = 40.783282, step = 0.000001, format="%0.6f")
drop_long = st.number_input("Input the dropoff longitude", value = -73.984365, step = 0.000001, format="%0.6f")
drop_lat = st.number_input("Input the dropoff latitude",value = 40.769802, step = 0.000001, format="%0.6f")
passenger = st.number_input("Input the number of passengers", step=1, value = 2)



'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...


3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
paramns = {
    "pickup_datetime": f"{date} {time}",
    "pickup_longitude": long,
    "pickup_latitude": lat,
    "dropoff_longitude": drop_long,
    "dropoff_latitude": drop_lat,
    "passenger_count": passenger
}


response = requests.get(url, params=paramns)
st.write(response.json())
