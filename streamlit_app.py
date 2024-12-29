import streamlit as st
from PIL import Image
import mysql.connector
from mysql.connector import Error

# Database credentials
DB_HOST = '192.95.14.153'
DB_USER = 'webbuilderuser'
DB_PASSWORD = 'm7xXGk6scyBv1iPORvmJ'
DB_NAME = 'Rest'

# Streamlit app
st.title("MySQL Database Table Viewer")

def connect_to_database():
    """
    Connect to the MySQL database using the provided credentials.
    Returns the connection object.
    """
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        if connection.is_connected():
            st.success("Connected to the database successfully!")
            return connection
    except Error as e:
        st.error(f"Error while connecting to the database: {e}")
        return None

def get_table_names(connection):
    """
    Fetch the names of all tables in the database.
    """
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        return [table[0] for table in tables]
    except Error as e:
        st.error(f"Error while fetching table names: {e}")
        return []

# Main logic
connection = connect_to_database()

if connection:
    table_names = get_table_names(connection)
    if table_names:
        st.subheader("Tables in the Database:")
        st.write(table_names)
    else:
        st.warning("No tables found in the database.")
    connection.close()
else:
    st.error("Could not connect to the database.")


st.title("stlite sharing: Serverless Streamlit app platform")

st.markdown("""

### stlite
**stlite** is a port of _Streamlit_ to Wasm, powered by Pyodide,
that runs completely on web browsers.

image = Image.open('stlitelogo.png')
st.image(image, caption='stlite logo')

The official repository is [🔗 here](https://github.com/whitphx/stlite).

If you are new to Streamlit, read the Getting Started tutorial [🔗 here](https://docs.streamlit.io/library/get-started) first
(don't worry, it only takes a few minutes 👍),
but **you can skip the "Installation" section** because you are here 😎.
You can start writing code right out of the box on this online editor 👈!
(If there is not an editor on the left, you are seeing the shared app.
Navigate to the editor mode: https://edit.share.stlite.net/)

### stlite sharing
This page is built on **stlite sharing**, an online code editor & sharing platform for _stlite_. \\
If you see the editor and preview panes side by side, you are in the editor mode, https://edit.share.stlite.net/. \\
If you see only this Streamlit app, you are in the sharing mode, https://share.stlite.net/.
(If you want to edit the app, please go to the [editor mode](https://edit.share.stlite.net/)!)

The app code and data are encoded into the URL as a hash like 'https://share.stlite.net/#!ChBz...',
so you can save, share and restore the app only this the URL.
If you are on the editor page, click the "Open App" link on the top right toolbar to see the standalone app!

You can switch the editor and sharing modes by replacing the host naem in the URL,
'edit.share.stlite.net' and 'share.stlite.net'.

### Tell your story!
When you create some apps with _stlite_, please share it!
All you need to do is copy and paste the URL 👍

* **stlite** GitHub Discussions [🔗 here](https://github.com/whitphx/stlite/discussions/categories/show-and-tell)
* Streamlit community forum [🔗 here](https://discuss.streamlit.io/)

""")

st.header("Streamlit Component Samples")

st.markdown("""
    All these features are working on your browser!
""")

name = st.text_input("Your name?")
st.write("Hello,", name or "world", "!")

value = st.slider("Value?")
st.write("The slider value is", value)

import numpy as np
import pandas as pd

st.subheader("Chart Sample")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

# tab1, tab2, tab3 = st.tabs(["Line chart", "Area chart", "Bar chart"])
# with tab1:
#     st.line_chart(chart_data)
# with tab2:
#     st.area_chart(chart_data)
# with tab3:
#     st.bar_chart(chart_data)

st.subheader("DataFrame Sample")
df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df)

st.subheader("Camera input")
st.info("Don't worry! The photo data is processed on your browser and never uploaded to any remote servers.")
enable_camera_input = st.checkbox("Use the camera input")
if enable_camera_input:
    picture = st.camera_input("Take a picture")

    if picture:
        st.image(picture)
