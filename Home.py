# Import the necessary libraries
import streamlit as st
import pandas

# Set the page configuration to a wide layout
st.set_page_config(layout="wide")

# Create two columns for the content
col1, col2 = st.columns(2)

# Add an image to the first column
with col1:
    st.image("images/photo.jpg")

# Add a title and info box to the second column
with col2:
    st.title("Dotan Frenkel")
    content = """
    Hi, I'm Dotan and I'm a python developer.\n
    I enjoy creating applications that are user-friendly and solve real-world problems.\n
    I have experience in building various types of apps with python.\n
    Trough programming my own projects i gain practical experience which you can find them here below."
    """
    st.info(content)

# Create a container for additional content
content2 = st.container()
with content2:
    st.write("""
    Below you can find some of the apps I have built in Python. Feel free to contact me!
    """)

# Divide the page into three columns for the app displays
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

# Load the data from a CSV file using pandas
df = pandas.read_csv("data.csv")

# Display the first 10 apps in the left column
with col3:
    for index, row in df[:10].iterrows():
        # Display the title, description, image, and source code link for each app
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

# Display the remaining apps in the right column
with col4:
    for index, row in df[10:].iterrows():
        # Display the title, description, image, and source code link for each app
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
