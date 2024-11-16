import numpy as np
import pandas as pd

def preprocess_eeg_data(eeg_data, window_length=10, window_overlap=3):
    """
    Preprocess raw EEG data for testing models by windowing and cleaning data.

    Args:
        eeg_data (np.ndarray or pd.DataFrame): The raw EEG data array (n_samples, n_features).
        window_length (int): Length of the window for feature extraction.
        window_overlap (int): Overlap size between consecutive windows.

    Returns:
        np.ndarray: Processed EEG data shaped for model input (n_windows, n_features, 1).
    """
    import numpy as np

    # Remove NaN values
    print(f"eeg_data.shape: {eeg_data.shape}")
    if isinstance(eeg_data, pd.DataFrame):
        clean_data = eeg_data.dropna().to_numpy()
    else:
        clean_data = eeg_data[~np.isnan(eeg_data).any(axis=1)]
    print(f"clean_data shape: {clean_data.shape}")

    # Compute number of windows based on windowing parameters
    num_samples = clean_data.shape[0]
    step = window_length - window_overlap
    num_windows = (num_samples - window_length) // step + 1
    print("num_windows:", num_windows)

    # Window the data to extract mean features
    features_list = []
    for i in range(num_windows):
        start = i * step
        end = start + window_length
        window_features = np.mean(clean_data[start:end, :], axis=0)
        features_list.append(window_features)

    # Stack features into a 3D array (n_windows, n_features, 1)
    processed_data = np.expand_dims(np.array(features_list), axis=-1)

    return processed_data
