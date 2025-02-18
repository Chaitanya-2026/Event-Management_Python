import streamlit as st
import view, add, update, delete
import session

# Initialize session state
session.initialize_session()


st.title("Event Management System")
menu = st.sidebar.selectbox("Menu", ["View Events", "Add Event", "Update Event", "Delete Event"])

if menu == "View Events":
    view.view_events()
elif menu == "Add Event":
    add.add_event()
elif menu == "Update Event":
    update.update_event()
elif menu == "Delete Event":
    delete.delete_event()
