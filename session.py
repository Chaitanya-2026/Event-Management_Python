import streamlit as st

def initialize_session():
    if 'events' not in st.session_state:
        st.session_state.events = [{"id": 1, "name": "Birthday Party"}, {"id": 2, "name": "Conference"}, {"id": 3, "name": "College Annual Day Celebrations"}]
