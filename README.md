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
