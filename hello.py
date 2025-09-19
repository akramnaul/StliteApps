import streamlit as st

# Inject CSS
st.markdown("""
    <style>
    .container {
        margin: 50px auto 40px auto;
        width: 600px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Hello Streamlit with Custom CSS")
st.write("This is styled using injected CSS.")
