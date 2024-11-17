import pandas as pd
import streamlit as st
from PIL import Image
import time
import random #for the random number generator (testing purpose)
import base64
import streamlit.components.v1 as components
from streamlit.components.v1 import html
import os

# Import the main function from main.py
from EmotionDetectionPipeline.main import main

st.title("System to Detect Personality Mood Based on EEG Signals")

#placeholder
title = st.empty()
user_prompt = st.empty()
Self_assesment = st.empty()
Caregiving = st.empty()

#I need to change it back to new version
# user = "old"
user = "new"

if user == "old":
    happy_image = Image.open("./assets/happy.png")
    anger_image = Image.open("./assets/negative.png")
    neutral_image = Image.open("./assets/neutral.png")
    neutral_music = "./assets/forest.mp3"
    happy_music = "./assets/happy.mp3"

if user == "new":
    happy_image = Image.open("./GUI/assets/happy.png")
    anger_image = Image.open("./GUI/assets/negative.png")
    neutral_image = Image.open("./GUI/assets/neutral.png")
    neutral_music = "./GUI//assets/forest.mp3"
    happy_music = "./GUI//assets/happy.mp3"

st.header("What are you using this application for?")
option = st.selectbox(
    "",
    ["", "Caregiving", "Self-assesment"],
    key="selected"
)

#Music Playing
st.session_state.keep_playing = True
FREQ = 1

#assesment
st.session_state.running_assesment = False

#function for reading the file and return user's current emotion
def read_emotion():
    #create progress bar
    label = main()

    #pop up text to show the user that we got the emotion data

    if label == 0:
        st.write(label)
        return "negative"
    elif label == 1:
        st.write(label)
        return "neutral"
    elif label == 2:
        st.write(label)
        return "positive"
    else:
        st.write("Something went wrong. Check your conenction")
    
    
    

def change_frequency(container, current_emotion):
    music_freq = 1

    if container == Caregiving:
        if current_emotion == "neutral":
            music_freq = FREQ/2
        elif current_emotion == "negative":
            music_freq = FREQ/10
    #If self-assesment
    else:
        if current_emotion == "positive":
            music_freq = FREQ/2
        elif current_emotion == "negative":
            music_freq = FREQ*2

    html_code = f"""
                <script> 
                    var myaudio = window.parent.document.getElementById("audio1");
                    myaudio.playbackRate = {music_freq}
                </script> 
                """
    html(html_code)
    return music_freq


def change_emoji(image, current_emotion):
    if current_emotion == "positive":
        image.image(happy_image)

    elif current_emotion == "neutral":
        image.image(neutral_image) #this should be neutral image
    elif current_emotion == "negative":
        image.image(anger_image)
    else:
        st.write("something went wrong please try agiain")
    return image

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio id='audio1' controls autoplay>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

col3, col4, col5, col6 = st.columns([1,1,1,1])

def run_the_assesment(selected):
    #change the target based on the user's selection
    if selected == "Caregiving":
        target = "Your patient's"
        container = Caregiving
    elif selected == "Self-assesment":
        target = "Your"
        container = Self_assesment
    else:
        st.warning("Please select one of the options", icon="⚠️")
        return


    with col4: 
        stop_button = st.button("Stop the assesment", key="stop_music")
    with col5: 
        if st.button("Change music"):
            music = st.file_uploader("Upload your audio file", type="mp3")

    #I will use Javascript audio tag since it allows us to play/stop the music and change the speed of the music
    autoplay_audio(neutral_music) #we shuold allow the user to pick whatever music they want to play
    
    text = st.empty() #initialize text container
    image = st.empty() #image container

    #Loop until the user wants to stop the music
    while st.session_state.keep_playing == True:
        st.write("emotion updated")
        current_emotion = read_emotion()
        print("emotion updated")
        col6, col7 = st.columns(2)
        with col6:
            change_emoji(image, current_emotion)
        with col7: 
            text.subheader(f"{target} current emotion is {current_emotion}")
        change_frequency(container, current_emotion)

        if stop_button:
            st.session_state.keep_playing = False
            st.session_state.running_assesment = False
            html_code = """
                <script> 
                    var myaudio = window.parent.document.getElementById("audio1");
                    myaudio.pause();
                   // myaudio.currentTime = 0;  // Reset to beginning if you want
                </script> 
                """
            html(html_code)

    container.empty()
    
#Initialize the user's currenet emotion
current_emotion = read_emotion()

col6, col8 = st.columns([5, 1])

if option is not "":
    #Start the assesment
    with col3:
        if st.button("Start the assesment", key="start"):
            with col6:
                run_the_assesment(option)