import streamlit as st

st.header("This is a button :)")

#st.button("Say hello!")

if st.button("Say hello!"):
    st.write("Hello all!")

else:
    st.write("Click the button ^^")