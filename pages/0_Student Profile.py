import streamlit as st

#st.set_page_config(page_title="Animation Demo", page_icon="📹")
# st.markdown("# Student Profile")
st.header("Student Profile")
st.write("Welcome new student! Your first task is to complete your profile!")

col1, col2 = st.columns(2)
with col1:
    st.text_input("First Name")
    st.text_input("Student ID")
    st.selectbox("Major",['Select one','Computer Science', 'Electrical Enginnering','Civil Enginnering',"Mathematics"])
    st.text_input("Telephone Number")
    st.text_input("Course Prefere")
with col2:
    st.text_input("Last Name")
    st.text_input("Student Email")
    st.selectbox("Classification",['Select one','Freshman','Sophomore','Junior','Senior'])
st.multiselect("Course Preferences",['Psychology','Sociology','Biology','Chemistry'])
st.button('Submit')

st.chat_message("Do you have any general advising questions?")
st.chat_input()