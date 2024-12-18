import streamlit as st
from datetime import time, datetime

st.header("Let's make different sliders")

# Exemple 1 - age
age = st.slider(label = "Your age?", min_value = 0, max_value = 110, step = 1)
st.write("I am ", age, " years old :)")

# Exemple 2 - tranche d'age
# value = valeur default
age_range = st.slider(label = "Your age range?", min_value = 0, max_value = 100, value = (20,49))
st.write("My age range is ", age_range, " !")

# Exemple 3 - RDV
rdv = st.slider(label = "Select your appointment", value = (time(11,30), time(12,45)), format = "hh:mm")
st.write("Your appointment is set at ", rdv)

# Exemple 4 - RDV-2
rdv_2 = st.slider(label = "Select your appointment", value = (time(11,30)))
st.write("Your appointment starts at ", rdv_2)

# Exemple 5 - date début
start_time = st.slider(
    "When do you start?",
    value=datetime(2024, 12, 18, 9, 30),
    format="MM/DD/YY - hh:mm",
)
st.write("Start time:", start_time)