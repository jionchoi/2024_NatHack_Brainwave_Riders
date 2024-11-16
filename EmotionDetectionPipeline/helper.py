import numpy as np
import pandas as pd
from scipy.signal import butter, lfilter


# Function to create a bandpass filter
def bandpass_filter(data, lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return lfilter(b, a, data)


# Function to extract EEG frequency bands and save to DataFrame
def process_eeg_data(eeg_data, sampling_rate):
    # Frequency bands in Hz
    bands = {
        "Delta": (1, 4),
        "Theta": (4, 8),
        "Alpha": (7.5, 13),
        "Beta": (13, 30),
        "Gamma": (30, 44)
    }

    # Channel labels corresponding to the Muse EEG device
    channel_labels = ['TP9', 'AF7', 'AF8', 'TP10']

    # Initialize a dictionary to store the filtered signals and raw signals
    data_dict = {}

    # Extract each frequency band for all channels
    for band_name, (low, high) in bands.items():
        for i, channel in enumerate(channel_labels):
            filtered_signal = bandpass_filter(eeg_data[i, :], low, high, sampling_rate)
            data_dict[f"{band_name}_{channel}"] = filtered_signal

    # Add the raw data to the dictionary
    for i, channel in enumerate(channel_labels):
        data_dict[f"RAW_{channel}"] = eeg_data[i, :]

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data_dict)

    return df
