# ☁️ Intelligent Cloud Auto-Scaling using Reinforcement Learning

This project presents an **intelligent cloud auto-scaling system** that compares traditional threshold-based scaling with a **reinforcement learning (RL)-based approach** under dynamic workloads.  
The system is designed to model **elastic resource provisioning, cost optimization, and SLA constraints** in cloud computing environments.

An interactive web-based interface is deployed using **Streamlit Cloud** to visualize system behavior and performance metrics.

---

## 🚀 Features

- Threshold-based auto-scaling (baseline)
- Reinforcement Learning–based auto-scaling
- **Safety-Constrained RL** with SLA enforcement
- Multi-workload simulation (steady, bursty, periodic, random)
- SLA-aware cost modeling
- Predictive workload hinting
- Multi-objective reward optimization
- Interactive Streamlit dashboard
- Cloud deployment with real-time visualization

---

## 🏗️ System Architecture

The system consists of the following components:

- **Workload Generator**: Simulates dynamic traffic patterns
- **Cloud Environment**: Models elastic VM resources, cost, and SLA constraints
- **Auto-Scaling Engine**:
  - Threshold-based policy
  - RL-based policy with safety guard
- **Evaluation Module**: Measures response time, cost, and SLA violations
- **Web Interface**: Interactive visualization using Streamlit

---

## 🧠 Methodology

The reinforcement learning agent observes:
- Resource utilization
- Active VM count
- Predicted workload trend

Actions include:
- Scale up
- Scale down
- Maintain current resources

A **multi-objective reward function** balances:
- Response time
- Resource cost
- SLA violation penalties

To ensure reliability, a **rule-based SLA safety guard** enforces service guarantees during decision-making.

---

## 📊 Evaluation Metrics

- Average Response Time
- Operational Cost
- Number of Active VMs
- SLA Violations

The RL-based approach demonstrates improved responsiveness and reduced SLA violations compared to the threshold-based baseline, at the cost of higher resource utilization.

---

## 🌐 Live Demo

The project is deployed on **Streamlit Cloud**:

🔗 *Live URL*: `https://cloud-autoscaling-rl-ak4n3kzxhazigsxgy2cj9t.streamlit.app`



---

## 🛠️ Tech Stack

- Python
- NumPy
- Matplotlib
- Streamlit
- GitHub + Streamlit Cloud

---

## ▶️ Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py
