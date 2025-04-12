import streamlit as st
import re

def Password_meter():
    st.set_page_config(page_title="🔐 Password Strength Meter")
    
    st.title("Password Strength Meter 🌡")
    
    st.markdown(
        "<h3 style='color:red;'>Check your password security 🔑</h3></br>",
        unsafe_allow_html=True
    )

    user_Name = st.text_input("**Enter your full name:**")
   

    if user_Name:
        if len(user_Name) >= 4 and " " not in user_Name:
            st.success(f"**{user_Name}** username saved!")
        else:
            st.warning("It should be more than **4** characters & it should not contain **spaces**")
            

    check_password = st.text_input(
        "**Test your password now!**",
        help="You'll get a password score (1-5) & feedback based on strength rules.",
        type="password"
    )
    st.divider()

    score = 0
    checker_Feedback = []

    if check_password:
        if len(check_password) >= 8:
            score += 1
        else:
            checker_Feedback.append("✒ Password should be greater than 8 characters")

        if re.search('[A-Z]', check_password) and re.search('[a-z]', check_password):
            score += 1
        else:
            checker_Feedback.append("✒ Use both upper & lower case for a strong password")

        if re.search(r'\d', check_password):
            score += 1
        else:
            checker_Feedback.append("✒ Password should contain at least one digit")

        if re.search(r'[!_@#\-^&*$]', check_password):
            score += 1
        else:
            checker_Feedback.append("✒ Password should contain at least one special character {! _ @ # - $ ^ & *}")

        if user_Name and user_Name in check_password:
            checker_Feedback.append("🚫 Never use your username in the password")
        else:
            score += 1

        
        if score == 5:
            checker_Feedback.append("✅ **Strong Password!**")
        elif score == 4:
            checker_Feedback.append("🔒 **Secure Password - but could be stronger.**")
        elif score == 3:
            checker_Feedback.append("⚠️ **Moderate Password - consider adding more security features.**")
        else:
            checker_Feedback.append("❌ **Weak Password - try creating a new one using suggestions above.**")

        # Show final result
        st.info(f"Your Score: {score} / 5")

        if checker_Feedback:
            st.write("## Feedback Suggestions 🔍")
            for suggestion in checker_Feedback:
                st.write(suggestion)


if __name__ == '__main__':
    Password_meter()


