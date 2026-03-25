import numpy as np
import pandas as pd
import os

os.makedirs("data", exist_ok=True)

# Simulated data duration
duration = 10  # seconds
sampling_rate = 100  # Hz (100 samples per second)
t = np.linspace(0, duration, duration * sampling_rate)

# === Normal Hand Movement ===
# Small, smooth fluctuations (mild noise)
x_normal = np.sin(0.5 * t) + np.random.normal(0, 0.05, len(t))
y_normal = np.cos(0.5 * t) + np.random.normal(0, 0.05, len(t))
z_normal = 1 + np.random.normal(0, 0.02, len(t))
tremor_index_normal = np.abs(np.random.normal(0.02, 0.01, len(t)))

normal_df = pd.DataFrame({
    "Time(s)": t,
    "X": x_normal,
    "Y": y_normal,
    "Z": z_normal,
    "Tremor_Index": tremor_index_normal
})
normal_df.to_csv("data/normal_hand.csv", index=False)

# === Tremor Hand Movement ===
# Add fast oscillations (like small repetitive shakes)
x_tremor = np.sin(0.5 * t) + 0.3 * np.sin(15 * t) + np.random.normal(0, 0.08, len(t))
y_tremor = np.cos(0.5 * t) + 0.3 * np.sin(15 * t + np.pi/4) + np.random.normal(0, 0.08, len(t))
z_tremor = 1 + 0.2 * np.sin(15 * t + np.pi/2) + np.random.normal(0, 0.03, len(t))
tremor_index_tremor = np.abs(np.random.normal(1.2, 0.3, len(t)))  # higher values

tremor_df = pd.DataFrame({
    "Time(s)": t,
    "X": x_tremor,
    "Y": y_tremor,
    "Z": z_tremor,
    "Tremor_Index": tremor_index_tremor
})
tremor_df.to_csv("data/tremor_hand.csv", index=False)

print("✅ Generated: data/normal_hand.csv and data/tremor_hand.csv")
