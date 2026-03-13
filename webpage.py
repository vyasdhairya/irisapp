import streamlit as st
st.title("Iris Prediction")
import pickle
model=pickle.load(open("model_iris.pkl","rb"))
sl=st.slider("Sl",2.0,10.0)
sw=st.slider("Sw",2.0,10.0)
pl=st.slider("pl",2.0,10.0)
pw=st.slider("pw",2.0,10.0)
if st.button("Predict"):
    st.success(model.predict([[sl,sw,pl,pw]]))