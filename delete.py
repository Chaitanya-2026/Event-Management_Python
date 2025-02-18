import streamlit as st
import session

def delete_event():
    st.subheader("Delete Event")
    event_id = st.number_input("Enter Event ID to Delete", min_value=1, step=1)
    if st.button("Delete Event"):
        st.session_state.events = [event for event in st.session_state.events if event["id"] != event_id]
        st.success(f"Event ID {event_id} deleted successfully!")
