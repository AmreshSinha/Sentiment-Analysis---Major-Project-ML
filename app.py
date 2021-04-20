import streamlit as st
import sklearn
import joblib
model = joblib.load('Coursera Review Sentiment')
st.title('Coursera Review Sentiment')
ip = st.text_input('Enter your review')
op = model.predict([ip])
if st.button('Predict'):
  temp = op[0]
  if temp==5:
    st.title("Loved It! (Rating: 5)")
  elif temp==4:
    st.title("It's Good (Rating: 4)")
  elif temp==3:
    st.title("It's Neutral (Rating: 3)")
  elif temp==2:
    st.title("It's Bad (Rating: 2)")
  elif temp==1:
    st.title("It's the worst course User have ever seen! (Rating: 1)")
