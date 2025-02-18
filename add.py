import streamlit as st
import session

def add_event():
    st.subheader("Add Event")
    event_name = st.text_input("Enter Event Name")
    if st.button("Add Event"):
        if event_name:
            new_id = len(st.session_state.events) + 1
            st.session_state.events.append({"id": new_id, "name": event_name})
            st.success(f"Event '{event_name}' added successfully!")
        else:
            st.error("Event name cannot be empty!")
