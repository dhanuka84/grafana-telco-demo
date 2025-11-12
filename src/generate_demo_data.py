import pandas as pd
import numpy as np
import random
import time
from datetime import datetime, timedelta

# --- [1] DEMO CONFIGURATION ---
# Change these values to alter the "story" of your demo

SIMULATION_DURATION_HOURS = 3      # How many hours of data to generate
DATA_INTERVAL_SECONDS = 60         # A data point every 60 seconds (1 minute)
INCIDENT_START_MINUTE = 60         # The incident starts 60 minutes into the simulation
INCIDENT_END_MINUTE = 120          # The incident ends 120 minutes in (1 hour duration)

# --- [2] ENTITY DEFINITIONS ---
TOWERS = {
    "gNB-4401-A": {"sector": "Sector_A", "base_util": 40.0, "base_sinr": 20.0},
    "gNB-4402-B": {"sector": "Sector_B", "base_util": 30.0, "base_sinr": 18.0}, # <<< OUR PROBLEM TOWER
    "gNB-4403-C": {"sector": "Sector_C", "base_util": 50.0, "base_sinr": 22.0},
}

USERS = []
for i in range(150):
    USERS.append({
        "id": f"user_{i+1:03d}",
        "tower_id": random.choice(list(TOWERS.keys())), # Assign user to a random tower
        "app_in_use": random.choice(["Video", "VoIP", "Gaming", "Web"])
    })

# --- [3] DATA GENERATION ---

print("Starting time-series data generation...")

# Calculate total simulation time and steps
end_time = datetime.now()
start_time = end_time - timedelta(hours=SIMULATION_DURATION_HOURS)
total_seconds = (end_time - start_time).total_seconds()
total_steps = int(total_seconds / DATA_INTERVAL_SECONDS)

# Incident start/end times relative to the simulation start
incident_start_time = start_time + timedelta(minutes=INCIDENT_START_MINUTE)
incident_end_time = start_time + timedelta(minutes=INCIDENT_END_MINUTE)

# Lists to hold all our data points
ran_data = []
cem_data = []
business_data = []

# Main simulation loop
for i in range(total_steps):
    current_timestamp = start_time + timedelta(seconds=i * DATA_INTERVAL_SECONDS)
    
    # Check if we are in the "incident" window
    is_incident = (current_timestamp >= incident_start_time) and \
                  (current_timestamp < incident_end_time)
    
    # --- Generate RAN (Cell Tower) Metrics ---
    generated_ran_metrics = {} # To store this loop's values for CEM correlation
    for tower_id, data in TOWERS.items():
        # Add normal random noise
        util = data["base_util"] + random.uniform(-5, 5)
        sinr = data["base_sinr"] + random.uniform(-2, 2)

        # !!! THIS IS THE INCIDENT !!!
        if is_incident and tower_id == "gNB-4402-B":
            util = 98.5 + random.uniform(0, 1)  # Critically high congestion
            sinr = 2.0 + random.uniform(0, 1)    # Critically low quality
        
        # Add to our list for the CSV
        ran_data.append({
            "timestamp": current_timestamp,
            "tower_id": tower_id,
            "sector": data["sector"],
            "prb_utilization": max(0, min(100, util)),
            "avg_sinr": max(0, sinr),
        })
        # Store for use in CEM generation
        generated_ran_metrics[tower_id] = {"prb_utilization": util, "avg_sinr": sinr}

    # --- Generate CEM (Customer) Metrics ---
    # *** THIS IS THE CRITICAL CORRELATION ***
    for user in USERS:
        tower_metrics = generated_ran_metrics[user["tower_id"]]
        
        # Customer MOS score is a function of their tower's signal quality (SINR)
        mos_score = 1.0 + (tower_metrics["avg_sinr"] / 22.0) * 4.0
        
        # Buffering is a function of tower congestion (utilization)
        buffer_rate = (tower_metrics["prb_utilization"] / 100.0) * 30.0
        
        # Add noise to make it realistic
        mos_score = max(1, min(5, mos_score + random.uniform(-0.3, 0.3)))
        buffer_rate = max(0, buffer_rate + random.uniform(0, 3))
        
        cem_data.append({
            "timestamp": current_timestamp,
            "user_id": user["id"],
            "tower_id": user["tower_id"], # The correlation key!
            "app_in_use": user["app_in_use"],
            "call_mos_score": mos_score,
            "video_buffer_rate": buffer_rate
        })

    # --- Generate Business (Sector-level) Metrics ---
    # We only need to generate this once per timestamp, for each sector
    for sector_name in ["Sector_A", "Sector_B", "Sector_C"]:
        churn_risk = 4.5 + random.uniform(-0.2, 0.2)
        tickets = 3 + random.choice([0, 1])

        # !!! BUSINESS IMPACT OF THE INCIDENT !!!
        if is_incident and sector_name == "Sector_B":
            churn_risk = 18.2 + random.uniform(-1, 1) # Sector B churn spikes
            tickets = 28 + random.choice([-2, 0, 2])    # Support tickets for Sector B spike
        
        business_data.append({
            "timestamp": current_timestamp,
            "sector": sector_name,
            "churn_risk_percent": churn_risk,
            "new_support_tickets": tickets
        })

print("Data generation complete. Converting to DataFrames...")

# --- [4] SAVE TO CSV FILES ---
df_ran = pd.DataFrame(ran_data)
df_cem = pd.DataFrame(cem_data)
df_business = pd.DataFrame(business_data)

# Save to CSV
df_ran.to_csv('ran_metrics.csv', index=False)
df_cem.to_csv('cem_metrics.csv', index=False)
df_business.to_csv('business_metrics.csv', index=False)

print("\nSuccessfully generated 3 files:")
print(f" - ran_metrics.csv ({len(df_ran)} rows)")
print(f" - cem_metrics.csv ({len(df_cem)} rows)")
print(f" - business_metrics.csv ({len(df_business)} rows)")
print("\nNext step: Upload these files to a public GitHub Gist.")
