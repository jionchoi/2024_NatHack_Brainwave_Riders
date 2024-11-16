import streamlit as st
from PIL import Image
import time
import random #for the random number generator (testing purpose)
import base64 #for audio playing
import streamlit.components.v1 as components
st.title("System to Detect Personality Mood Based on EEG Signals")


#placeholder
title = st.empty()
user_prompt = st.empty()
Self_assesment = st.empty()
Caregiving = st.empty()

#I need to change it back to new version
# user = "old"
user = "new"

#TO-DO: 
#Add play/stop button for the music in case the user wants to stop listening to the music

if user == "old":
    sad_image = Image.open("./assets/sad.png")
    happy_image = Image.open("./assets/happy.png")
    anger_image = Image.open("./assets/angry.png")
    fear_image = Image.open("./assets/fear.png")
    sadness_image = Image.open("./assets/Sadness.png")
    neutral_music = "./assets/relaxing.mp3"
    happy_music = "./assets/happy.mp3"

if user == "new":
    sad_image = Image.open("./GUI/assets/sad.png")
    happy_image = Image.open("./GUI/assets/happy.png")
    anger_image = Image.open("./GUI/assets/angry.png")
    fear_image = Image.open("./GUI/assets/fear.png")
    sadness_image = Image.open("./GUI/assets/Sadness.png")
    neutral_music = "./GUI//assets/relaxing.mp3"
    happy_music = "./GUI//assets/happy.mp3"

col1, col2 = st.columns(2)

if 'current_emotion' not in st.session_state:
    st.session_state.current_emotion = "Sad"

if 'mode_index' not in st.session_state:
    st.session_state.mode_index = None

if 'responses' not in st.session_state:
    st.session_state.responses = []

if 'final_decision_made' not in st.session_state:
    st.session_state.final_decision_made = False

if 'output_index' not in st.session_state:
    st.session_state.output_index = 0 

# clarification_questions = [
#     ("Do you feel physically tired?", "Sadness"),
#     ("Are you feeling overwhelmed with responsibilities?", "Fear"),
#     ("Have you had enough sleep recently?", "Sadness"),
#     ("Do you feel a lack of motivation?", "Anger"),
#     ("Are you experiencing physical discomfort (e.g., headache)?", "Anger")
# ]

st.header("What are you using this application for?")
option = st.selectbox(
    "",
    ["", "Caregiving", "Self-assesment"],
    key="selected"
)

#Music Playing
st.session_state.keep_playing = True
FREQ = 1

#function for reading the file and return user's current emotion
def read_emotion():
    current_emotion = ""
    time.sleep(1)
    number = random.randrange(1,10)
    if number < 4:
        current_emotion= "negative"
    elif number > 7:
        current_emotion= "positive"
    else:
        current_emotion= "neutral"

    return current_emotion

def change_frequency(container, current_emotion):
    music_freq = 1

    if container == Caregiving:
        if current_emotion == "neutral":
            music_freq = FREQ/2
            # st.markdown(f"""
            #     <script>
            #         myaudio = document.getElementById("audio1");
            #         myaudio.playbackRate = {}
            #     </script>
            # """)
        elif current_emotion == "negative":
            music_freq = FREQ/10
    #If self-assesment
    else:
        if current_emotion == "positive":
            music_freq = FREQ/2
        elif current_emotion == "negative":
            music_freq = FREQ*2

    return music_freq

def change_emoji(image, current_emotion):
    if current_emotion == "positive":
        image.image(happy_image)
    elif current_emotion == "neutral":
        image.image(fear_image) #this should be neutral image
    else:
        image.image(anger_image)

    return image

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio id='audio1' controls>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )

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

    col3, col4, col5 = st.columns([1,1,2])
    with col3: 
        stop_button = st.button("Stop the assesment", key="stopp")
    with col4: 
        if st.button("Change music"):
            music = st.file_uploader("Upload your audio file")

    #I will use Javascript audio tag since it allows us to play/stop the music and change the speed of the music
    autoplay_audio(neutral_music) #we shuold allow the user to pick whatever music they want to play

    text = st.empty() #initialize text container
    image = st.empty() #image container

    #Loop until the user wants to stop the music
    while st.session_state.keep_playing == True:
        current_emotion = read_emotion()
        col6, col7 = st.columns(2)
        with col6:
            change_emoji(image, current_emotion)
        with col7: 
            text.subheader(target + " current emotion is " + current_emotion)
        change_frequency(container, current_emotion)

        if stop_button:
            st.session_state.keep_playing = False
            html_code = """
                <p> Music is not playing </p>
                <script> 
                    var myaudio = document.getElementsByTagName("audio")[0];
                   
                     myaudio.pause();
                      myaudio.currentTime = 0;  // Reset to beginning if you want
                </script> 
                """
            components.html(

                html_code, height=200
            )

    container.empty()

#Few things to decide, are we going to change the music based on the emotion or only the freqency of the music. Or both. Is it even possible to change the frequence of the music?
    
#Initialize the user's currenet emotion
current_emotion = read_emotion()

#Start the assesment
run_the_assesment(option)

# col3, col4 = st.columns(2)

# with col1:
#     emotion_images = {
#         "Sad": sad_image,
#         "Happy": happy_image,
#         "Anger": anger_image,
#         "Fear": fear_image,
#         "Sadness": sadness_image
#     }
#     st.image(emotion_images[st.session_state.current_emotion])

# output = [1,1,0,0,1,1]


# with col2:
#     # if st.session_state.mode_index is None:
#         st.header("Select the work mode")
#         if st.button("Self-assesment") or st.session_state.mode_index == 0:

#             # =====================
#             st.session_state.mode_index = 0
#             st.session_state.music_playing = True  
#             # st.audio("./GUI/assets/relaxing.mp3", start_time=0, autoplay=True) 
#             while st.session_state.output_index < len(output):
#                 current_output = output[st.session_state.output_index]

#                 # Play the corresponding music
#                 if current_output == 1:
#                     st.audio(neutral_music, start_time=0, autoplay=True)
#                     st.write("Playing neutral music.")
#                 elif current_output == 0:
#                     st.audio(happy_music, start_time=0, autoplay=True)
#                     st.write("Playing happy music.")
                
#                 # Update the index and wait
#                 st.session_state.output_index += 1
#                 time.sleep(5)
#                 st.rerun()
            
#             # st.audio(neutral_music, start_time=0)
#             # st.write("Playing music to cheer you up!")
#             # st.session_state.current_emotion = "Happy"
#             # st.session_state.final_decision_made = False
#             # st.session_state.mode_index = 0
            
#             # =====================
#             if st.button("Return to Home"):
#                 st.session_state.question_index = None    
#                 st.session_state.responses = [] 
#                 st.session_state.mode_index = None
#             time.sleep(5)
#             st.rerun()    

#         elif st.button("Healthcare giver"):
#             st.session_state.question_index = 2
#             st.session_state.responses = []
#             st.session_state.final_decision_made = False

#             if st.button("Return to Home"):
#                 st.session_state.question_index = None    
#                 st.session_state.responses = [] 
#                 st.session_state.mode_index = None

#     # elif st.session_state.question_index < len(clarification_questions):
#     #     current_question, emotion = clarification_questions[st.session_state.question_index]
#     #     st.header(current_question)

#     #     # "Yes" and "No" buttons for answering the question
#     #     col_yes, col_no = st.columns(2)
#     #     with col_yes:
#     #         if st.button("Yes"):
#     #             st.session_state.responses.append(emotion)
#     #             st.session_state.question_index += 1
#     #             st.rerun()

#     #     with col_no:
#     #         if st.button("No"):
#     #             st.session_state.responses.append(None)
#     #             st.session_state.question_index += 1
#     #             st.rerun()

#     # elif not st.session_state.final_decision_made:
#     #     emotion_count = {"Anger": 0, "Fear": 0, "Sadness": 0}
#     #     for response in st.session_state.responses:
#     #         if response:
#     #             emotion_count[response] += 1

#     #     dominant_emotion = max(emotion_count, key=emotion_count.get)
#     #     st.session_state.current_emotion = dominant_emotion
#     #     st.session_state.final_decision_made = True
#     #     st.rerun()

#     # if st.session_state.final_decision_made:
#     #     st.header(f"You are likely feeling: {st.session_state.current_emotion}")
#     #     if st.button("Return to Home"):
#     #         st.session_state.question_index = None
#     #         st.session_state.responses = []
#     #         st.session_state.current_emotion = "Sad"
#     #         st.session_state.final_decision_made = False