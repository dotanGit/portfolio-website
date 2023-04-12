import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)   # there 2 option in streamlit container and col

with col1:   # in order to access the col/container you start with "with"
    st.image("images/photo.jpg")   # REMEMBER- st means streamlit so each time im calling this library for its modules
with col2:
    st.title("Dotan Frenkel")
    content = """
    Hi my name is dotan , im 25 years old from Israel
    """
    st.info(content)   # info give me a box around my text its only for style i can use here write or text also
content2 = st.container()
with content2:
    st.write("""
Below you can find some of the apps i have built in Python. Feel free to contact me!
""")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])   # if i want space between the columns i add an empty column and set the sizes of each column
df = pandas.read_csv("data.csv")   # pandas library allow me to connect into other files such as csv and make some action with this file

with col3:
    # create the column with a title and an image ,
    # the for loop goes through each row and row["somthing"] represent from which column we want to take the data
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    # create the column with a title and an image ,
    # the for loop goes through each row and row["somthing"] represent from which column we want to take the data
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")