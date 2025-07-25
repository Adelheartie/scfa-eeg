# -*- coding: utf-8 -*-
"""SCFA.1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vAU9caAW3zvJMyMNEyKH-0-WYCKYKX7q
"""

from google.colab import drive
drive.mount('/content/drive')

from scipy.io import loadmat
import numpy as np

eeg_path = '/content/drive/MyDrive/eeg project/Subject01_s1.mat'
mat_data = loadmat(eeg_path)
run = mat_data['run']

# Extract main tuple
main_struct = run[0][0]
inner_tuple = main_struct  # The tuple containing EEG and metadata

# EEG data
eeg_data = inner_tuple[0]
print("✅ EEG data shape:", eeg_data.shape)

# Metadata
metadata_array = inner_tuple[1]
metadata_raw = metadata_array[0][0]

# Sample rate
sample_rate = metadata_raw[2][0][0]
print("✅ Sample rate:", sample_rate)

# Channel names
channel_info_raw = metadata_raw[3][0]
channel_names = [c[0] for c in channel_info_raw]
print("✅ First 10 channel names:", channel_names[:10])

# Events
events_raw = metadata_raw[4][0]
event_positions = events_raw[0][0]
event_types = events_raw[1][0]
print("✅ First 5 event positions:", event_positions[:5])
print("✅ First 5 event types:", event_types[:5])

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 4))
plt.plot(eeg_data[:, 0])  # Plot first channel
plt.title(f"EEG signal from channel {channel_names[0]}")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.show()

run = mat_data['run']

# Check what is inside the main block
for i, item in enumerate(run[0][0]):
    print(f"Index {i}: Type: {type(item)}")

print(run[0][0][0])

# Check what exactly is in run[0][0]
print("run[0][0] type:", type(run[0][0]))
print("run[0][0]:", run[0][0])

# Get the inner tuple that has EEG and metadata
inner_struct = main_struct[0]

print("Length of inner_struct:", len(inner_struct))
print("Type of inner_struct[0]:", type(inner_struct[0]))

# EEG data (first item)
eeg_data = inner_struct[0]
print("✅ EEG data shape:", eeg_data.shape)

# Metadata (second item)
metadata_array = inner_struct[1]

# Metadata array is deeply nested: array([[(array([...metadata...]))]])
metadata_raw = metadata_array[0][0]

# Sample rate
sample_rate = metadata_raw[2][0][0]
print("✅ Sample rate:", sample_rate)

# Channel names
chan_info_raw = metadata_raw[3][0]
channel_names = [c[0] for c in chan_info_raw]
print("✅ First 10 channel names:", channel_names[:10])

# Events
events_raw = metadata_raw[4][0]
event_positions = events_raw[0][0]
event_types = events_raw[1][0]
print("✅ First 5 event positions:", event_positions[:5])
print("✅ First 5 event types:", event_types[:5])