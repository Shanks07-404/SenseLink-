import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# === File Paths ===
NORMAL_PATH = "data/normal_hand.csv"
TREMOR_PATH = "data/tremor_hand.csv"
OUTPUT_LOG = "data/vitals_analysis_log.csv"

# === Helper: Calculate Tremor Ratio ===
def calculate_tremor_ratio(df):
    if "Tremor_Index" not in df.columns:
        raise ValueError("CSV must contain a 'Tremor_Index' column.")
    ratio = np.mean(df["Tremor_Index"])
    return round(ratio, 4)

# === Helper: Classify Based on Tremor Ratio ===
def classify_tremor(ratio):
    if ratio < 0.05:
        return "✅ Normal Motion"
    elif ratio < 0.1:
        return "⚠️ Mild Irregularity"
    else:
        return "❗ Tremor Detected"

# === Plot Graph for Comparison ===
def plot_vitals(normal_df, tremor_df):
    plt.figure(figsize=(12, 6))
    plt.title("Hand Movement: Normal vs Tremor")
    plt.plot(normal_df["Time(s)"], normal_df["Tremor_Index"], label="Normal", alpha=0.8)
    plt.plot(tremor_df["Time(s)"], tremor_df["Tremor_Index"], label="Tremor", alpha=0.8)
    plt.xlabel("Time (s)")
    plt.ylabel("Tremor Index")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

# === Main Function ===
def main():
    print("📊 Analyzing vitals from CSV files...\n")

    # Load CSVs
    if not os.path.exists(NORMAL_PATH) or not os.path.exists(TREMOR_PATH):
        print("❌ Error: Missing CSV files. Please make sure normal_hand.csv and tremor_hand.csv exist in the data folder.")
        return

    normal_df = pd.read_csv(NORMAL_PATH)
    tremor_df = pd.read_csv(TREMOR_PATH)

    # Compute tremor ratios
    normal_ratio = calculate_tremor_ratio(normal_df)
    tremor_ratio = calculate_tremor_ratio(tremor_df)

    # Classify
    normal_status = classify_tremor(normal_ratio)
    tremor_status = classify_tremor(tremor_ratio)

    # Display Results
    print("=== Tremor Analysis Results ===")
    print(f"Normal File Tremor Ratio: {normal_ratio} → {normal_status}")
    print(f"Tremor File Tremor Ratio: {tremor_ratio} → {tremor_status}")

    # Log to CSV
    results = pd.DataFrame([
        {"File": "normal_hand.csv", "Tremor_Ratio": normal_ratio, "Status": normal_status},
        {"File": "tremor_hand.csv", "Tremor_Ratio": tremor_ratio, "Status": tremor_status}
    ])
    results.to_csv(OUTPUT_LOG, index=False)

    print(f"\n📝 Results saved to {OUTPUT_LOG}")

    # Plot the graph
    plot_vitals(normal_df, tremor_df)

if __name__ == "__main__":
    main()
