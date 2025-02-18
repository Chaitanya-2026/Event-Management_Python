import streamlit as st
import session

def update_event():
    st.subheader("Update Event")
    event_id = st.number_input("Enter Event ID to Update", min_value=1, step=1)
    new_name = st.text_input("Enter New Event Name")
    if st.button("Update Event"):
        for event in st.session_state.events:
            if event["id"] == event_id:
                event["name"] = new_name
                st.success(f"Event ID {event_id} updated successfully!")
                break
        else:
            st.error("Event ID not found!")
