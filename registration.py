import streamlit as st 
import requests



def main():
    st.title("Please! login details")
    
    menu=["Login","Signup"]

    choice=st.sidebar.selectbox("Menu",menu)
    
    if choice=="Login":
        status = st.sidebar.radio("Select: ", ('Login', 'Verify'))
        venueid=""
        password=""

        if (status == 'Login'):
               venueid=st.sidebar.text_input("userid ID")
               password=st.sidebar.text_input("Password",type='password')
        else:
             r = requests.post("http://46.137.221.124:5000/login_venue", data={'ven_id': venueid, 'password': password})
             if r.status_code==200:
                 otp=st.sidebar.text_input("OTP")
                 if st.sidebar.button("Verify"):
                     r1 = requests.post("http://46.137.221.124:5000/verifyVenueOTP", data={'ven_id': venueid, 'otp': otp})
                     if r1.status_code==200:
                         st.subheader("Welcome!")
                         
                     
    
        
    elif choice=="Signup":
        status = st.sidebar.radio("Select: ", ('Register Info', 'Verify'))
        venuename=""
        venueid=""
        password=""
        pname=""
        email=""
        phonenum=""
        lat=""
        long=""
        venbeacon=""

        if (status == 'Register Info'):
            venuename=st.sidebar.text_input("Venue Name")
            venueid=st.sidebar.text_input("userid ID")
            password=st.sidebar.text_input("Password",type='password')
            pname="Gay"
            email=st.sidebar.text_input("Email")
            phonenum=st.sidebar.text_input("Phone Number")
            lat=856.35
            long=96.250
            venbeacon="895236998564646a4678"
        
        else:
            r = requests.post("http://46.137.221.124:5000/register_venue", data={'ven_f_name':venuename,'ven_id': venueid, 'password': password, 'ven_beacon':venbeacon, 'password': password, 'pname':pname, 'email':email, 'ph_no':phonenum, 'lat':lat, 'long':long})
            if r.status_code==200:
                otp=st.sidebar.text_input("OTP")
                if st.sidebar.button("Verify"):
                    r1 = requests.post("http://46.137.221.124:5000/verifyVenueOTP", data={'ven_id': venueid, 'otp': otp})
                    if r1.status_code==200:
                        st.subheader("Welcome!")
        
         
            
if __name__ == "__main__":
    main()