# import pyttsx3
# import streamlit as st

# # Initialize text-to-speech engine
# speaker = pyttsx3.init()
# # change the speaker's voice
# speaker.setProperty('voice', 'english+f3')
# # Create a text area where the user can input the text to be converted
# text = st.text_area("Enter the text to be converted to an audio file:", height=400)

# # Create a button that the user can click to convert the text to an audio file
# if st.button("Convert to MP3"):
#     # Save the text as an MP3 audio file
#     speaker.save_to_file(text, "converted_text.mp3")
#     # Play the audio file
#     speaker.runAndWait()
#     # Stop the audio engine
#     speaker.stop()
#     st.audio("converted_text.mp3")
    
    
# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio
mytext = 'Welcome to geeksforgeeks!'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")

# Playing the converted file
os.system("mpg321 welcome.mp3")