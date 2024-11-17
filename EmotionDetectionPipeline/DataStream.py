from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from brainflow.data_filter import DataFilter, FilterTypes
import numpy as np
import time
from EmotionDetectionPipeline.helper import process_eeg_data
import pandas as pd

def collect_eeg_data(
    serial_port="Bluetooth-Incoming-Port",
    board_id=38,
    save_path="data/eeg_data.csv",
    stream_duration=5
):
    """
    Collect EEG data from a Muse BCI device and save it as a CSV file.

    Args:
        serial_port (str): The serial port for the Muse device (e.g., "Bluetooth-Incoming-Port").
        board_id (int): The Board ID (e.g., 38 for Muse).
        save_path (str): The path to save the CSV file with processed data.
        stream_duration (int): The duration (in seconds) for streaming EEG data.

    Returns:
        pd.DataFrame: A DataFrame containing the processed EEG data.
    """
    # Initialize BrainFlow input parameters
    params = BrainFlowInputParams()
    params.serial_port = serial_port

    # Initialize board
    try:
        board = BoardShim(board_id, params)
        board.prepare_session()
        print("Successfully prepared the physical board")
    except Exception as e:
        print("Device cannot be found:", e)
        return None

    # Start streaming data
    print("Starting Stream")
    board.start_stream()
    time.sleep(stream_duration)  # Wait for the specified duration
    data = board.get_board_data()  # Retrieve all data and clear the internal buffer
    print("Ending Stream")
    board.stop_stream()
    board.release_session()

    # Isolate EEG data
    eeg_channel_names = BoardShim.get_eeg_names(board_id)
    print(f"EEG Channels: {eeg_channel_names}")
    eeg_channels = board.get_eeg_channels(board_id)
    eeg_data = data[eeg_channels]
    print(f"EEG Data Shape: {eeg_data.shape}")  # Shape should be (n_channels, n_samples)

    # Process the EEG data
    sampling_rate = board.get_sampling_rate(board_id)
    df = process_eeg_data(eeg_data, sampling_rate)

    # # Save processed data to CSV
    # df.to_csv(save_path, index=False)
    # print(f"EEG data saved to {save_path}")

    return df
