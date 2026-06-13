import streamlit as st

if st.button("Click Me"):
    st.write("Button Clicked")

if st.checkbox("Check me to show some text"):
    st.write("You're seeing this text because you checked the checkbox")

user_input = st.text_input("Enter text", "Sample text")
st.write("You enterd:", user_input)

age = st.number_input("Enter Your Age", min_value=0, max_value=100)
st.write(f"Your age is: {age}")

message = st.text_area("Enter a message")
st.write(f"Your message: {message}")

choice = st.radio("Pick one", ["Choice 1", "Choice 2","Choice 3",])
st.write(f"You chose: {choice}")

if st.button("Success"):
    st.success("Operaction was successful")

try:
    1/0
except Exception as e:
    st.exception(e)