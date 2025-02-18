import streamlit as st
import session

def view_events():
    st.subheader("View Events")
    if not st.session_state.events:
        st.write("No events to display.")
    else:
        for event in st.session_state.events:
            st.write(f"ID: {event['id']}, Name: {event['name']}")
