
import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    # st.set_page_config(
    #     page_title="Welcome"
    # )
    st.title("Howard University Bison Advisor!")

    #st.sidebar.success("")
    st.text("Please log in below")
    st.text_input("Email")
    st.text_input("Password")
    st.button("Log in")



if __name__ == "__main__":
    run()
