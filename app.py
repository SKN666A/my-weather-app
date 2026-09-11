import streamlit as st
import requests

# Page Configuration
st.set_page_config(page_title="Weather App", page_icon="🌤️")

st.title("👦 Real-Time Weather App")
st.write("Enter your city name to check the live weather!")

# User Input
city = st.text_input("City Name:", "Lahore")

# Secure API Key fetching using st.secrets
api_key = st.secrets.get("OPENWEATHER_API_KEY")

if st.button("Check Weather"):
    if not api_key:
        st.error("API Key nahi mili! Pehle secrets.toml mein key add karein.")
    else:
        # OpenWeatherMap API Call
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            weather_desc = data['weather'][0]['description']
            
            # Weather Metrics Display
            st.success(f"Weather fetched for {city.title()}!")
            col1, col2 = st.columns(2)
            col1.metric("Temperature", f"{temp} °C")
            col2.metric("Humidity", f"{humidity}%")
            st.info(f"Condition: **{weather_desc.title()}**")
            
        elif response.status_code == 401:
            st.warning("The features haven't been activated for 'Api' yet; there is still a bit of waiting time left for them!")
        else:
            st.error("No data found or an error occurred. Please check back!")
