import streamlit as st
import matplotlib.pyplot as plt
from main import run

st.set_page_config("Cloud Auto-Scaling Lab", layout="centered")
st.title("☁️ Intelligent Cloud Auto-Scaling Lab")

mode = st.selectbox("Workload Pattern", ["steady", "bursty", "periodic", "random"])
sla = st.slider("SLA Threshold", 2.0, 6.0, 4.0)
epsilon = st.slider("RL Exploration (ε)", 0.05, 0.5, 0.2)

if st.button("Run Experiment"):
    m = run(mode, sla, epsilon)

    col1, col2 = st.columns(2)
    col1.metric("Threshold SLA Violations", m["th_sla"])
    col2.metric("RL SLA Violations", m["rl_sla"])

    def plot(a, b, title):
        fig, ax = plt.subplots()
        ax.plot(a, label="Threshold")
        ax.plot(b, label="RL")
        ax.set_title(title)
        ax.legend()
        st.pyplot(fig)

    plot(m["th_rt"], m["rl_rt"], "Response Time")
    plot(m["th_cost"], m["rl_cost"], "Cost")
    plot(m["th_vms"], m["rl_vms"], "VM Count")
