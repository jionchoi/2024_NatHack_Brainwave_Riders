import streamlit as st
from PIL import Image

st.title("System to Detect Personality Mood Based on EEG Signals")

# Load the images
sad_image = Image.open("./GUI/assets/sad.png")
happy_image = Image.open("./GUI/assets/happy.png")
anger_image = Image.open("./GUI/assets/angry.png")
fear_image = Image.open("./GUI/assets/fear.png")
sadness_image = Image.open("./GUI/assets/Sadness.png")

col1, col2 = st.columns(2)

if 'current_emotion' not in st.session_state:
    st.session_state.current_emotion = "Sad"

if 'question_index' not in st.session_state:
    st.session_state.question_index = None

if 'responses' not in st.session_state:
    st.session_state.responses = []

if 'final_decision_made' not in st.session_state:
    st.session_state.final_decision_made = False

clarification_questions = [
    ("Do you feel physically tired?", "Sadness"),
    ("Are you feeling overwhelmed with responsibilities?", "Fear"),
    ("Have you had enough sleep recently?", "Sadness"),
    ("Do you feel a lack of motivation?", "Anger"),
    ("Are you experiencing physical discomfort (e.g., headache)?", "Anger")
]

with col1:
    emotion_images = {
        "Sad": sad_image,
        "Happy": happy_image,
        "Anger": anger_image,
        "Fear": fear_image,
        "Sadness": sadness_image
    }
    st.image(emotion_images[st.session_state.current_emotion], use_container_width=True)


with col2:
    if st.session_state.question_index is None:
        st.header("How can I help you?")
        if st.button("Play music"):
            st.write("Playing music to cheer you up!")
            st.session_state.current_emotion = "Happy"
            st.session_state.final_decision_made = False

        elif st.button("Clarify my emotional state"):
            st.session_state.question_index = 0
            st.session_state.responses = []
            st.session_state.final_decision_made = False

    elif st.session_state.question_index < len(clarification_questions):
        current_question, emotion = clarification_questions[st.session_state.question_index]
        st.header(current_question)

        # "Yes" and "No" buttons for answering the question
        col_yes, col_no = st.columns(2)
        with col_yes:
            if st.button("Yes"):
                st.session_state.responses.append(emotion)
                st.session_state.question_index += 1
                st.rerun()

        with col_no:
            if st.button("No"):
                st.session_state.responses.append(None)
                st.session_state.question_index += 1
                st.rerun()

    elif not st.session_state.final_decision_made:
        emotion_count = {"Anger": 0, "Fear": 0, "Sadness": 0}
        for response in st.session_state.responses:
            if response:
                emotion_count[response] += 1

        dominant_emotion = max(emotion_count, key=emotion_count.get)
        st.session_state.current_emotion = dominant_emotion
        st.session_state.final_decision_made = True
        st.rerun()

    if st.session_state.final_decision_made:
        st.header(f"You are likely feeling: {st.session_state.current_emotion}")
        if st.button("Return to Home"):
            st.session_state.question_index = None
            st.session_state.responses = []
            st.session_state.current_emotion = "Sad"
            st.session_state.final_decision_made = False
