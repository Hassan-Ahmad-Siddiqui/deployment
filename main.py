import streamlit as st

st.title("Streamlit App")

user_input = st.text_input("Enter some text:")

if st.button("Show Text"):
    # Display the user input
    st.write(f"You entered: {user_input}")
