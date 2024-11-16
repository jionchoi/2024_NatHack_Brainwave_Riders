import numpy as np
import pickle
from collections import Counter
from EmotionDetectionPipeline.DataStream import collect_eeg_data
from EmotionDetectionPipeline.DataPreprocessing import preprocess_eeg_data

def main():
    try:
        # EEG data collection
        print("Starting EEG data collection...")
        df = collect_eeg_data(
            serial_port="Bluetooth-Incoming-Port",
            board_id=38,
            save_path="data/eeg_data.csv",
            stream_duration=5  # Record for 5 seconds
        )
        if df is None:
            raise RuntimeError("Data collection failed. No data was collected.")
        print("Successfully collected EEG data")

        # Data preprocessing
        print("Starting data preprocessing...")
        preprocessed_data = preprocess_eeg_data(df, window_length=10, window_overlap=3)
        if preprocessed_data is None or preprocessed_data.size == 0:
            raise RuntimeError("Data preprocessing failed. Processed data is empty.")
        print("Successfully preprocessed EEG data")

        # Load best model
        print("Loading the best model...")
        try:
            with open('model/best_model', 'rb') as f:
                rf = pickle.load(f)
        except FileNotFoundError:
            raise RuntimeError("Model loading failed. File 'model/best_model' not found.")
        except Exception as e:
            raise RuntimeError(f"Model loading failed: {str(e)}")
        print("Successfully loaded the best model")

        # Predict using the model
        print("Making predictions...")
        predicted_labels = rf.predict(np.squeeze(preprocessed_data))

        # Majority voting
        label_counts = Counter(predicted_labels)
        most_common_label, count = label_counts.most_common(1)[0]

        # Save predicted labels to a CSV file
        np.savetxt("data/predicted_labels.csv", [most_common_label], delimiter=",", fmt='%f')
        print("Predicted labels saved to 'data/predicted_labels.csv'")

    except RuntimeError as e:
        print(f"Process aborted: {str(e)}")

if __name__ == "__main__":
    main()
