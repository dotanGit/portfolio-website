import streamlit as st
from send_email import send_email
import pandas

st.header("Contact Me")

df = pandas.read_csv("topics.csv")


with st.form(key="email_forms"):
    user_email = st.text_input("Please enter your email address")
    option = st.selectbox("What topic do you want to discuss?", df)
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: Message from Python Portfolio

From: {user_email}

Topic: {option}

Message:
{raw_message}
"""
    button = st.form_submit_button("Submit")   # the default of button is False and when someone presses it its True - it is a boolean variable
    if button:   # the default of button is False and when someone presses it its True - it is a boolean variable
        send_email(message)
        st.info("Your message was sent ")