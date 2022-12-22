import pyttsx3
import streamlit as st

SPEAKER_LIST = {
    'Voice 1 (Female)': 'en_0',
    'Voice 2 (Male)': 'en_29',
    'Voice 3 (Female)': 'en_41',
    'Voice 4 (Male)': 'en_110'
}

# Initialize text-to-speech engine
speaker = pyttsx3.init()
# change the speaker's voice
speaker.setProperty('voice', 'english+f3')
# Create a text area where the user can input the text to be converted
text = st.text_area("Enter the text to be converted to an audio file:", height=400)
st.header('2. Please select voice')
speaker = st.radio('Available voices:', SPEAKER_LIST.keys(), horizontal=True)
# Create a button that the user can click to convert the text to an audio file
if st.button("Convert to MP3"):
    # Save the text as an MP3 audio file
    speaker.save_to_file(text, "converted_text.mp3")
    # Play the audio file
    speaker.runAndWait()
    # Stop the audio engine
    speaker.stop()
    st.audio("converted_text.mp3")
    