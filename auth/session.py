import streamlit as st

def login_user(username):
    st.session_state["authenticated"] = True
    st.session_state["username"] = username

def logout_user():
    st.session_state["authenticated"] = False
    st.session_state["username"] = None
    st.st.rerun()

def is_logged_in():
    return st.session_state.get("authenticated", False)

def logout_button():
    st.sidebar.markdown(f"👋 Logged in as `{st.session_state.get('username')}`")
    if st.sidebar.button("🚪 Logout"):
        logout_user()
