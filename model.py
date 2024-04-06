import cohere
import streamlit as st

co = cohere.Client('SvMpSTWkpUfpZkzWB4OAx7kWdsDARN4gVO24Qq6I') # This is your trial API key


user_inputs = st.text_input('What type of a plant/tree are you looking for?')
inputs = []
if st.button("Get recommendation"):
    response = co.classify(
    model='e7cd0c96-a994-46ab-be86-cd3fe11d5809-ft',
    inputs=inputs,
    examples=[])
    predictions =response.classifications[0].predictions
    formatted_predictions = []


    formatted_predictions.append("The best trees for you are:\n")
    for i, prediction in enumerate(predictions, start=1):
        formatted_predictions.append(f"{i}. {prediction}")
    numbered_list = "\n".join(formatted_predictions)
    st.write(numbered_list)

