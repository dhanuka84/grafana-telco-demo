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

---

## How to Use This Project

### 1. Prerequisites

You must have Python 3 installed on your computer.

### 2. Install Dependencies

In your terminal, install the required Python packages:

```bash
pip install -r requirements.txt
