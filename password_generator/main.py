import streamlit as st
import random
import string

st.set_page_config(
    page_title="Password Generator application",
    page_icon="🔐",                 
        
)

        

def password_generator(length,use_digits,use_special):
    character = string.ascii_letters  # provide upper & lower case
    
    if use_digits:
        character += string.digits 

    if use_special: 
        character += string.punctuation # provide all special character

    return ''.join(random.choice(character) for _ in range(length))


st.title("🏁Password Generator application")
st.markdown(
        "<h3 style='color:darkgreen;'>🔒 Need a strong password? Get one instantly!</h3></br>",
        unsafe_allow_html=True
    )

use_special = st.checkbox("Include special")

use_digits = st.checkbox("Include digits")

length = st.slider("\nSelect pasword length",min_value=8, max_value=28,value=15)

if st.button("Create password"):
    generate = password_generator(length,use_digits,use_special)

    
    st.markdown(f"""<div style='padding:12px; margin-bottom:16px; border-radius:8px; background-color:#f4f9f4; border:1px solid #4caf50;'>
        <p style='font-weight:bold; color:#1b5e20; font-size:16px;'>
            🔑 Your Password: 
                <span style="color:#e91e63;">{generate}</span>
        </p>
    </div>""", unsafe_allow_html=True)

    if length > 12 and use_digits and use_special:
        st.success("✅ The password you generated is strong and secure.")

