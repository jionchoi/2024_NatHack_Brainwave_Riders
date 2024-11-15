import streamlit as st
from PIL import Image
import time
st.title("System to Detect Personality Mood Based on EEG Signals")

user = "old"
# user = "new"

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

with col1:
    emotion_images = {
        "Sad": sad_image,
        "Happy": happy_image,
        "Anger": anger_image,
        "Fear": fear_image,
        "Sadness": sadness_image
    }
    st.image(emotion_images[st.session_state.current_emotion])

output = [1,1,0,0,1,1]


with col2:
    # if st.session_state.mode_index is None:
        st.header("Select the work mode")
        if st.button("Self-assesment") or st.session_state.mode_index == 0:

            # =====================
            st.session_state.mode_index = 0
            st.session_state.music_playing = True  
            # st.audio("./GUI/assets/relaxing.mp3", start_time=0, autoplay=True) 
            while st.session_state.output_index < len(output):
                current_output = output[st.session_state.output_index]

                # Play the corresponding music
                if current_output == 1:
                    st.audio(neutral_music, start_time=0, autoplay=True)
                    st.write("Playing neutral music.")
                elif current_output == 0:
                    st.audio(happy_music, start_time=0, autoplay=True)
                    st.write("Playing happy music.")
                
                # Update the index and wait
                st.session_state.output_index += 1
                time.sleep(5)
                st.rerun()
            
            # st.audio(neutral_music, start_time=0)
            # st.write("Playing music to cheer you up!")
            # st.session_state.current_emotion = "Happy"
            # st.session_state.final_decision_made = False
            # st.session_state.mode_index = 0
            
            # =====================
            if st.button("Return to Home"):
                st.session_state.question_index = None    
                st.session_state.responses = [] 
                st.session_state.mode_index = None
            time.sleep(5)
            st.rerun()    





        elif st.button("Healthcare giver"):
            st.session_state.question_index = 2
            st.session_state.responses = []
            st.session_state.final_decision_made = False

            if st.button("Return to Home"):
                st.session_state.question_index = None    
                st.session_state.responses = [] 
                st.session_state.mode_index = None

    # elif st.session_state.question_index < len(clarification_questions):
    #     current_question, emotion = clarification_questions[st.session_state.question_index]
    #     st.header(current_question)

    #     # "Yes" and "No" buttons for answering the question
    #     col_yes, col_no = st.columns(2)
    #     with col_yes:
    #         if st.button("Yes"):
    #             st.session_state.responses.append(emotion)
    #             st.session_state.question_index += 1
    #             st.rerun()

    #     with col_no:
    #         if st.button("No"):
    #             st.session_state.responses.append(None)
    #             st.session_state.question_index += 1
    #             st.rerun()

    # elif not st.session_state.final_decision_made:
    #     emotion_count = {"Anger": 0, "Fear": 0, "Sadness": 0}
    #     for response in st.session_state.responses:
    #         if response:
    #             emotion_count[response] += 1

    #     dominant_emotion = max(emotion_count, key=emotion_count.get)
    #     st.session_state.current_emotion = dominant_emotion
    #     st.session_state.final_decision_made = True
    #     st.rerun()

    # if st.session_state.final_decision_made:
    #     st.header(f"You are likely feeling: {st.session_state.current_emotion}")
    #     if st.button("Return to Home"):
    #         st.session_state.question_index = None
    #         st.session_state.responses = []
    #         st.session_state.current_emotion = "Sad"
    #         st.session_state.final_decision_made = False