import streamlit as st
import json
import os
from auth.session import login_user

# 📂 File to store users
CREDENTIALS_FILE = "auth/users.json"

# 📥 Load saved users or use fallback
if os.path.exists(CREDENTIALS_FILE):
    with open(CREDENTIALS_FILE, "r") as f:
        USER_CREDENTIALS = json.load(f)
else:
    USER_CREDENTIALS = {
        "admin": "admin123",
        "guest": "guest123"
    }


def save_credentials():
    with open(CREDENTIALS_FILE, "w") as f:
        json.dump(USER_CREDENTIALS, f)


def check_login():
    if st.session_state.get("authenticated"):
        return True

    st.markdown("## 🔒 Please log in to access the app")

    # 👤 Login form
    with st.form("login_form", clear_on_submit=True):
        username = st.text_input("👤 Username")
        password = st.text_input("🔑 Password", type="password")
        submitted = st.form_submit_button("🔓 Login")

        if submitted:
            if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
                login_user(username)
                st.rerun()
            else:
                st.error("❌ Invalid username or password.")

    # ➕ Register form
    with st.form("register_form", clear_on_submit=True):
        st.markdown("## 📝 New user? Register here")
        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")
        register = st.form_submit_button("📥 Register")

        if register:
            if new_user in USER_CREDENTIALS:
                st.warning("⚠️ Username already exists.")
            elif not new_user or not new_pass:
                st.warning("⛔ Please enter both username and password.")
            else:
                USER_CREDENTIALS[new_user] = new_pass
                save_credentials()
                st.success("✅ Registration successful! Please log in.")

    return False
