import streamlit as st
import re
import sqlite3
import pandas as pd
conn = sqlite3.connect("data.db")
c = conn.cursor()
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable (firstname TEXT, lastname TEXT, mobile TEXT, email2 TEXT, AGE TEXT, password2 TEXT, confirnpassword TEXT)')
def add_userdata (FirstName, LastName, Mobile, Age, Email, password, Cpassword):
    c.execute('INSERT INTO userstable (firstname,lastname,mobile,email2, AGE ,password2,confirnpassword) VALUES (?,?,?,?,?,?,?)', (firstname, lastname, mobile,  email2, AGE ,password2,confirnpassword))
    conn.commit() 
def login_user(Email, password):
    c.execute('SELECT * FROM userstable WHERE email2 =? AND password2 = ?', (Email, password))
    data = c.fetchall()
    return data        
def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data
def delete_user(Email):
    c.execute("DELETE FROM userstable WHERE email2-" "*"+Email+"'")
    conn.commit()

def validate_email(email):
 pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
 return re.match(pattern, email) is not None
def validate_mobile(mobile):
 pattern = r'^\d{10}$'
 return re.match(pattern, mobile) is not None
def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True


select= st.sidebar.selectbox ("select: ",
                      ['home','signup','login'])
if select=="home":
    st.title("welcome to app")
    from PIL import Image
    img=Image.open("streamlit.jpg")
    st.image(img, width=200)
    st.text("this app is introduction of streamlit")
if select=="signup":  
    firstname = st.text_input("enter your first name",)
    lastname= st.text_input("enter your last name",)
    mobile = st.text_input("enter your mobile",)
    
    email2 = st.text_input("enter your email2",)
    AGE = st.slider("select the age",1,100)
    password2=st.text_input("enter your password2",type="password")
    confirnpassword=st.text_input("enter your confirmpassword",type="password")
    if  st.button("register"):
        if validate_email(email2):
            if  validate_mobile(mobile):
                if validate_password(password2):
                    create_usertable()
                    add_userdata(firstname,lastname, mobile, AGE , email2, password2,confirnpassword)
                    
                    st.success("Sucess Signup")
                else:
                    st.error("wrong password")
            else:
                st.error("wrong number")
        else:
          st.error("wrong email")  
                    
      
           
        
        
        
if select=="login" :
    email = st.sidebar.text_input("enter your email",)
    password=st.sidebar.text_input("enter your password",type="password")
    if st.sidebar.checkbox("submit"):
        result = login_user(email,  password)
        if result:
            st.success("Logged In as {}".format(email))
            email=st.text_input("Delete email")
            if st.button('Delete'):
                delete_user(email)
            user_result = view_all_users()
            clean_db =pd.DataFrame(user_result,columns=["firstName", "lastName", "mobile", "email2", "AGE", "password2", "Conifnpassword"])
            st.dataframe(clean_db)
            import pickle
            model=pickle.load(open("irissvm.pkl",'rb'))
            sl=st.slider("Select Sepal length",4.3,7.9)
            sw=st.slider("Select Sepal Width",2.0,4.4)
            pl=st.slider("Select Petal length",1.0,6.9)
            pw=st.slider("Select Petal Width",0.1,2.5)
            if st.button("Predict"):
                prd=model.predict([[float(sl),float(sw),float(pl),float(pw)]])
                st.success("The Class is="+prd[0])
   
        else:
           st.error("wrong eamil and password")
         
            
         
            
         
            
         
            
         
            
         
            
         

