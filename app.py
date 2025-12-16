import streamlit as st
from main import run_threshold, run_rl
import matplotlib.pyplot as plt

st.set_page_config(page_title="Cloud Auto-Scaling Simulator", layout="centered")

st.title("☁️ Cloud Auto-Scaling Simulation")
st.write("Comparison of Threshold-Based vs RL-Based Auto-Scaling")

if st.button("Run Simulation"):

    th_rt, th_cost, th_vms, th_sla = run_threshold()
    rl_rt, rl_cost, rl_vms, rl_sla = run_rl()

    st.subheader("📊 Performance Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Threshold Avg RT", f"{sum(th_rt)/len(th_rt):.2f}")
        st.metric("Threshold Avg Cost", f"{sum(th_cost)/len(th_cost):.2f}")
        st.metric("Threshold SLA Violations", th_sla)

    with col2:
        st.metric("RL Avg RT", f"{sum(rl_rt)/len(rl_rt):.2f}")
        st.metric("RL Avg Cost", f"{sum(rl_cost)/len(rl_cost):.2f}")
        st.metric("RL SLA Violations", rl_sla)

    st.subheader("📈 Response Time Comparison")
    fig1, ax1 = plt.subplots()
    ax1.plot(th_rt, label="Threshold")
    ax1.plot(rl_rt, label="RL-Based")
    ax1.legend()
    st.pyplot(fig1)

    st.subheader("📈 Cost Comparison")
    fig2, ax2 = plt.subplots()
    ax2.plot(th_cost, label="Threshold")
    ax2.plot(rl_cost, label="RL-Based")
    ax2.legend()
    st.pyplot(fig2)

    st.subheader("📈 VM Count Comparison")
    fig3, ax3 = plt.subplots()
    ax3.plot(th_vms, label="Threshold")
    ax3.plot(rl_vms, label="RL-Based")
    ax3.legend()
    st.pyplot(fig3)
