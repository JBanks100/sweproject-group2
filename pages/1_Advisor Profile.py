import streamlit as st

#st.set_page_config(page_title="Animation Demo", page_icon="📹")
# st.markdown("# Student Profile")
st.header("Advisor Profile")
st.write("Welcome advisor! Your first task is to complete your profile!")

col1, col2, col3 = st.columns(3)
with col1:
    st.text_input("Title")
with col2:
    st.text_input("First Name")
with col3:
    st.text_input("Last Name")

col21,col22 = st.columns(2)
with col21:
    st.text_input("Email")
    st.text_input("Office Location")
    st.selectbox("Department",['Select one','Computer Science', 'Electrical Enginnering','Civil Enginnering',"Mathematics"])
with col22:
    st.subheader("Office Hours")
    st.text_input("Monday")
    st.text_input("Tuesday")
    st.text_input("Wednesday")
    st.text_input("Thursday")
    st.text_input("Friday")

st.button('Submit')

st.chat_message("Do you have any general advising questions?")
st.chat_input()