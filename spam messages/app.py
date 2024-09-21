import streamlit as st
import pickle as pkl

model = pkl.load(open("model.pkl", 'rb'))

st.title('Predicting Spam Message')
message = st.text_input('Enter a message')
submit = st.button('Predict')
if submit:
    prediction = model.predict([message])

    if prediction[0] == "spam":
        st.warning('This is a spam message')
    else:
        st.success('This is legit message')
        st.balloons()