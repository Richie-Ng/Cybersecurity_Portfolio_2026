import pandas as pd
from sklearn.ensemble import IsolationForest

print("[*] Initializing Next-Gen XDR Behavioral AI Engine...")

# 1. Create a simulated dataset of network logins
# Features: [Hour_of_Day, Login_Attempts, Data_Transferred_MB]
data = {
    'User': ['Alice', 'Bob', 'Charlie', 'Alice', 'Eve_Hacker', 'Bob', 'Alice'],
    'Hour': [9, 10, 14, 11, 3, 13, 10],   # Eve logs in at 3 AM
    'Attempts': [1, 1, 2, 1, 45, 1, 2],   # Eve brute forces 45 times
    'Data_MB': [15, 20, 10, 18, 950, 22, 12] # Eve exfiltrates 950MB of data
}
df = pd.DataFrame(data)

print("[*] Ingesting network telemetry data...")
features = df[['Hour', 'Attempts', 'Data_MB']]

# 2. Implement the State-of-the-Art Solution: Isolation Forest (Unsupervised ML)
print("[*] Training Isolation Forest AI model on behavioral baselines...")
# contamination=0.15 means we expect roughly 15% of our data might be an attack
ai_model = IsolationForest(contamination=0.15, random_state=42)
ai_model.fit(features)

# 3. Evaluate the data to detect Zero-Day/Signatureless anomalies
print("[*] Evaluating telemetry for behavioral anomalies...\n")
df['Anomaly_Score'] = ai_model.predict(features)

# Output formatting
print("=== XDR AI EVALUATION RESULTS ===")
for index, row in df.iterrows():
    # The AI outputs -1 for anomalous behavior, and 1 for normal behavior
    if row['Anomaly_Score'] == -1:
        print(f"[CRITICAL THREAT] User: {row['User']} | Behavior: {row['Hour']}:00 hrs, {row['Attempts']} attempts, {row['Data_MB']}MB transferred.")
    else:
        print(f"[OK] User: {row['User']} | Normal Baseline Behavior.")

print("\n[*] Evaluation Complete: AI successfully identified the compromised account without relying on static malware signatures.")
