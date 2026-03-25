# SenseLink: AI Diagnostic Prototype
**Category:** Healthcare AI / Signal Processing

## Overview
SenseLink leverages signal-based anomaly detection to provide early risk estimation for Parkinson’s Disease. The system analyzes time-series data from wearable sensors and audio recordings to identify physiological patterns associated with the condition.

## Key Features
- **Signal Processing:** Implemented feature extraction for tremor frequencies and voice signals.
- **Anomaly Detection:** Utilizes Scikit-Learn models to identify deviations from healthy baselines.
- **Doctor-Facing Dashboard:** A full-stack demo featuring real-time analysis and visual diagnostic graphs.

## Tech Stack
**Frontend:** 
HTML, CSS, JavaScript

**Backend:**
Python, Flask (API + server)

**Data Processing & ML:**
NumPy, Pandas (data handling)
Librosa (voice signal analysis)
SciPy / basic signal processing (tremor detection)

**Data Input:**
CSV files (wearable sensor data)
WAV audio files (voice recordings)
