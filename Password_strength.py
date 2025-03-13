import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.markdown('''
<style>
            .main {text-align: center;}
            .stTextInput {width: 60% !important;}
            .stButton button {width: 50%; background-color: #eb4034; color: white; font-size: 18px;}
            .stButton button:hover {background-color: #ffffff;}
</style>
''', unsafe_allow_html=True)

st.title("\U0001F512 Password Strength Checker")
st.markdown("""
## Welcome to the ultimate password strength checker!👏  
Use this simple tool to check the strength of your password and get suggestions on how to make it stronger.  
We will give you helpful tips to create a **Strong Password** 🔒
""")

password = st.text_input("Enter Your Password", type="password")

if st.button("Check Strength"):
    feedback = []
    score = 0
    
    if password:
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("❌ Password should be at least 8 characters.")

        if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
            score += 1
        else:
            feedback.append("❌ Password should contain both upper and lower case characters.")

        if re.search(r"\d", password):
            score += 1
        else:
            feedback.append("❌ Password should contain at least one digit.")

        if re.search(r"[!@#$%^&*]", password):
            score += 1
        else:
            feedback.append("❌ Password should contain at least one special character (!@#$%^&*).")

        if score == 4:
            st.success("✔ Your Password is strong! 👍")
        elif score == 3:
            st.warning("🟠 Your Password is medium strength. It could be stronger.")
        else:
            st.error("🔴 Your password is weak. Please make it stronger.")

        if feedback:
            st.markdown("## Improvement Suggestions")
            for item in feedback:
                st.write(item)
    else:
        st.warning("Please enter a password first.")
