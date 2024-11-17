
# **EmoNeuro**  🫶 🧠 🤯 🎼 
**Bridge the Silence: an EEG-Based Emotional Assessment and Music Generation Platform**

To explore EmoCare and experience the platform's capabilities, visit our Streamlit app:
👉 [EmoNeuro](https://emoneuro.streamlit.app)
<img width="636" alt="Icon" src="https://github.com/user-attachments/assets/f6e5995e-ec9b-4ea6-8851-c739b9d122ef">


## **Overview**
EmoCare is an innovative platform developed by team Brainwave Riders during **natHACKS 2024** in Edmonton, Alberta, Canada. The platform is designed to detect users’ emotional state through real-time EEG data and provide adaptive personalized music. By combining advanced machine learning techniques, real-time data streaming, and intuitive user interfaces, EmoCare recognize and regulate emotions to bridge the gap between non-communicative individuals and their care providers as well as for self-assess emotions in healthy subjects.
<img width="1413" alt="Screenshot 2024-11-16 at 4 55 22 PM" src="https://github.com/user-attachments/assets/b8526273-6c72-41f7-8e02-59ab53f1f275">

### **Key Features**
- **EEG-Based Neural Feedback Loop**: Utilizes real-time brain activity to evaluate emotional states.  
- **Music Generation for Emotional Regulation**: Provides tailored music as:
  1. Emotion detection for enhanced communication (Increasing the sense of presence and personhood).
  2. A therapeutic/self-assessment tool for emotional balance.

---

## **Repository Structure**
The repository contains three primary components:

### **1. Machine Learning Model Training and Selection**
- File: `EmotionDetection_EEG_testMLModels.ipynb`
- **Models Considered**: Random Forest, GRU (Gated Recurrent Unit), SVM (Support Vector Machine), MLP (Multi-Layer Perceptron), and CFNN (Convolutional Fuzzy Layer Neural Network).  
- **Data Sources**: 
  - Open EEG dataset: [Feeling Emotions](https://www.kaggle.com/datasets/birdy654/eeg-brainwave-dataset-feeling-emotions)  
  - Onsite-collected data using Muse 2 [EEG_rawData.zip].  
- **Results**: Random Forest demonstrated the best performance with limited data samples, excelling in both cross-validation and transfer learning to novel subjects. The trained model is saved for deployment. ![untitled](https://github.com/user-attachments/assets/84a05653-c513-445b-9125-915445f024d0)


---

### **2. Real-Time EEG Data Streaming Pipeline**
- Folder: `EmotionDetectionPipeline`
- **Pipeline Overview**:
  - Uses **BrainFlow** for streaming EEG data from Muse 2.
  - Includes a configurable time-window smoothing preprocessor.
  - Outputs real-time emotional status predictions using the best-performing Random Forest model.
  
---

### **3. Graphical User Interface (GUI)**
- Built with **Streamlit** to provide a user-friendly experience.
- Enables seamless interaction with the EEG streaming pipeline and emotion-to-music transformation.

---

## **Getting Started**
### **Setup**
1. Clone this repository:
   ```bash
   git clone git@github.com:jionchoi/2024_NatHack_Brainwave_Riders.git
   cd 2024_NatHack_Brainwave_Riders
   ```
2. Create a virtual environment using the provided environment file:
   ```bash
   conda env create -f environment.yml
   conda activate emocare_env
   ```
3. Ensure your Muse 2 device is connected for real-time EEG data streaming.

---

## **Current Implementation**
- **Data Acquisition**: EEG signals are recorded using Muse 2.
<img width="636" alt="Feature_extraction" src="https://github.com/user-attachments/assets/b9459b70-bbd8-4d70-87be-b35ff44e0c3b">

- **Music Generation**: A baseline music segment is modified based on emotional goals. For example:
  - Amplifying certain frequency bands can evoke or regulate specific emotions.

---

## **Future Directions**
- Enhance music generation by incorporating large scale music generation models such as MusicGen, or providing access to Streaming platform such as Spotify
- Expand transfer learning capabilities to improve generalization across diverse user populations.
- Incorporate additional EEG devices for broader compatibility; including economical single-channel EEG headsets.

---

## **Contributors**
Developed by **Team Brainwave Riders** during natHACKS 2024.  (Submission on [**Devpost**]( https://devpost.com/software/brainwave-riders?ref_content=contribution-prompt&ref_feature=engagement&ref_medium=email&utm_campaign=contribution-prompt&utm_content=contribution_reminder&utm_medium=email&utm_source=transactional#app-team ))

To access our user friendly interface, please refer to:
(https://emoneuro.streamlit.app)
