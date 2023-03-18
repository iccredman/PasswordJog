#streamlit app setup
import streamlit as st 
import passwordjog

st.title("Password Jog")
st.write("Enter your account:")
account = st.text_input("", key="account")
print("Account is: " + str(account))

if st.button("Jog Me"):
 result = str(passwordjog.get_jog(account))
 st.write("Your password jog is:")
 print("Your password jog is: " + str(result))
 st.success(result)