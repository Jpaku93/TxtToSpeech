import streamlit as st
from gtts import gTTS

st.title("Text-to-Speech App")

# Get the text input from the user
text = st.text_input("Enter some text:")

if text:
    # Convert the text to speech
    tts = gTTS(text)

    # Save the audio file
    tts.save("output.mp3")

    # Display a link to the audio file
    st.audio("output.mp3")
