### **Use Case Title: 5G Customer Experience (CX) Assurance**

**"From Signal to Satisfaction: Correlating Network Health with Business Risk"**

#### **1\. The Business Challenge (The "Why")**

In telecommunications, data usually lives in silos:

* **Network Engineers** look at cell tower metrics (Signal Strength, Congestion).  
* **Customer Support** looks at trouble tickets.  
* **Executives** look at Churn Rate (customers leaving).

**The Problem:** When a cell tower degrades, engineers might see a "warning," but they don't know if actual humans are suffering. By the time the business realizes there's a problem (high churn or support calls), it is too late—the customers are already angry.

#### **2\. The Solution (Your Dashboard)**

This Grafana dashboard solves the "Silo Problem" by providing **Correlated Observability**. It joins data from three distinct layers into a single pane of glass:

1. **Infrastructure Layer:** Radio Access Network (RAN) health.  
2. **Service Layer:** Real-time Customer Experience (MOS scores, Video Buffering).  
3. **Business Layer:** Churn Risk and Support Volume.

---

#### **3\. The Demo Story (The "How")**

*When you present the dashboard, you are telling this specific story:*

**Scene 1: Normal Operations (Green State)**

* **Narrative:** "Here we see our network running normally. Our `Avg Network MOS Score` (Voice Quality) is **4.2**, which is excellent. Churn risk in all sectors is low (\< 5%). The network is healthy, and customers are happy."

**Scene 2: The Incident (The Root Cause)**

* **Narrative:** "Suddenly, we detect an anomaly in **Sector\_B**. Look at the **RAN Health** panel.  
  * Traffic on tower **`gNB-4402-B`** has spiked.  
  * **Congestion (PRB Utilization)** hit **98%**.  
  * **Interference (SINR)** dropped to **2 dB**.  
  * This is a technical failure."

**Scene 3: The Customer Impact (The Correlation)**

* **Narrative:** "In the past, we wouldn't know who this affected. But look at the **'Affected Customers'** table.  
  * Grafana has instantly correlated that tower failure to **50 specific users**.  
  * We can see their **Video Buffering** has jumped to **25%** and their **MOS Score** dropped below **2.0**.  
  * These people are trying to watch videos or make calls *right now* and failing."

**Scene 4: The Business Risk (The Consequence)**

* **Narrative:** "Because of this poor experience, look at the **'Churn Risk'** gauge for Sector B. It has spiked to **18%**.  
  * The **'New Support Tickets'** panel shows a surge in complaints from this specific area.  
  * The dashboard is telling us: *'Fix Tower 4402-B immediately, or you will lose these customers.'*"

---

#### **4\. Key KPIs Visualized**

* **Churn Risk %:** The probability of customers cancelling their contract based on recent experience.  
* **MOS Score (Mean Opinion Score):** A 1-5 rating of voice call quality (1=Bad, 5=Excellent).  
* **PRB Utilization:** How "full" the cell tower is (Network Congestion).  
* **SINR (Signal-to-Interference-plus-Noise Ratio):** The quality of the radio signal.

#### **5\. The Value Proposition**

By using this Grafana solution, the telecom operator moves from **Reactive** (waiting for complaints) to **Proactive** (fixing the network before the customer churns).


# Grafana Telco Demo Data Generator

This project generates three correlated CSV files to demonstrate a 5G Network Observability use case in Grafana. It simulates a "burning issue" where a cell tower (RAN) failure directly impacts customer experience (CEM) and business metrics (churn risk).

This dataset tells a complete story:
1.  **Normal Operations**
2.  **A Network Incident** (a specific tower gets congested)
3.  **The Customer Impact** (bad call quality and buffering for users on that tower)
4.  **The Business Impact** (churn risk and support tickets spike for that sector)
5.  **Recovery**

# Panel-by-Panel Explanation (Aligned With Telco CX Use Case)

## 1️⃣ Churn Risk -- \$sector (Gauge)

### What fields does it use?

-   sector
-   churn_risk_percent
-   timestamp

### Why these fields?

Because this panel answers: \> "What is the churn probability for this
sector right now?"

It filters the dataset by the chosen sector, then reduces all churn
values to a single number.

### Meaning

Shows business impact: unhappy customers → risk of churn.

------------------------------------------------------------------------

## 2️⃣ Avg. Network MOS Score (All Sectors) -- Gauge

### Fields

-   timestamp
-   call_mos_score

### Why?

This is a global KPI of voice quality across the entire network.

### Meaning

MOS shows customer perception. Drops during incidents, normal after
recovery.

------------------------------------------------------------------------

## 3️⃣ New Support Tickets -- \$sector (Stat Panel)

### Fields

-   sector
-   new_support_tickets
-   timestamp

### Why?

Shows real-time customer complaint volume.

### Meaning

Tickets spike when customers face issues → correlates experience to
complaints.

------------------------------------------------------------------------

## 4️⃣ RAN Health (Drill-Down) -- \$sector (Time Series)

### Fields

-   timestamp
-   tower_id
-   sector
-   avg_sinr
-   prb_utilization

### Why?

Shows radio layer behavior: interference + congestion + tower identity.

### Meaning

Reveals root cause at network level.

------------------------------------------------------------------------

## 5️⃣ Affected Customers (MOS \< 3.5) -- Filter by Tower (Table)

### Fields

-   timestamp
-   user_id
-   tower_id
-   app_in_use
-   call_mos_score
-   video_buffer_rate

### Why?

Identifies actual customers impacted and where.

------------------------------------------------------------------------

## 6️⃣ Business KPIs -- \$sector (Time Series)

### Fields

-   timestamp
-   sector
-   churn_risk_percent
-   new_support_tickets

### Why?

Shows business impact timeline before, during, after incident.

---

## How to Use This Project

### 1. Prerequisites

You must have Python 3 installed on your computer.

### 2. Install Dependencies

In your terminal, install the required Python packages:

```bash
pip install -r requirements.txt

--- 

### **`How to Do Your Demo Story`**

## 3. The Demo Story – *How to present it*

You’re not just clicking around a dashboard; you’re telling a story.

### Scene 1 – Normal Operations (“All Green”)

> “Here we see our network running normally.”

- **Avg. Network MOS Score** ≈ **4.2** (excellent).
- **Churn risk** in all sectors \< 5%.
- **RAN Health** shows stable SINR and moderate PRB utilization.
- **Affected Customers** table is empty (no severe issues).

👉 In Grafana:
- Set the time range to **Last 3 hours**.
- Drag-select the **first hour** of data on any time-series panel to zoom in.

---

### Scene 2 – The Incident (Technical Root Cause)

> “Now let’s see what happened around **10:05 AM**…”

- Zoom into the **middle hour** of the timeline.
- In **RAN Health**, focus on **Sector_B**:
  - Tower **`gNB-4402-B`** suddenly shows:
    - **PRB utilization** ≈ 98% (severe congestion).
    - **SINR** drops to around **2 dB** (poor signal quality).
- This is your **technical failure**.

The network layer sees a problem, but we’re not stopping there.

---

### Scene 3 – The Customer Impact (Experience Correlation)

> “Let’s see how this impacted real people.”

- Check **Avg. Network MOS Score**:
  - The gauge dips sharply during the incident window.
- Open **Affected Customers (MOS \< 3.5) – Filter by Tower**:
  - The table fills with ~50 users.
  - Their **MOS score** drops below **2.0**.
  - **Video buffering** jumps to around **25%**.
  - All of them are connected to **`gNB-4402-B`**.

👉 In Grafana:
- Use the **Tower ID** dropdown and select **`gNB-4402-B`**.
- The table now shows only the impacted users on that tower.

---

### Scene 4 – The Business Risk (Consequence)

> “Now, what does this mean for the business?”

- Look at **Churn Risk – Sector_B**:
  - The gauge spikes to ~**18%** during the incident.
- Look at **New Support Tickets – Sector_B**:
  - Ticket volume surges in the same time window.

The dashboard effectively says:

> **“Fix `gNB-4402-B` now – or you’re going to lose these customers.”**

Finally, zoom into the **last hour** to see the **recovery**:
- RAN metrics normalize.
- MOS scores improve.
- Churn risk and ticket volume return to baseline.

---

## 4. Key KPIs in the Dashboard

- **Churn Risk %**  
  Probability that customers in a sector will churn, derived from recent experience.

- **MOS Score (Mean Opinion Score)**  
  1–5 rating of perceived call quality  
  *(1 = Bad, 5 = Excellent).*

- **PRB Utilization (%)**  
  How “full” the cell tower is — a measure of RAN congestion.

- **SINR (dB)**  
  Signal-to-Interference-plus-Noise Ratio — how clean the radio signal is.

- **Video Buffer Rate (%)**  
  How much time video sessions spend buffering.

- **New Support Tickets**  
  Operational proxy for customer frustration.

---