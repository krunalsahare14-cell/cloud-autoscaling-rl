from cloud_env import CloudEnvironment
from workload import generate_workload
from threshold_scaling import threshold_policy
from rl_scaling import RLScaler
from plots import compare

SLA_THRESHOLD = 4.0


def run_threshold():
    cloud = CloudEnvironment()
    response_times, costs, vms = [], [], []
    sla_violations = 0

    for t in range(100):
        workload = generate_workload(t)
        utilization, response_time, cost = cloud.step(workload)

        if response_time > SLA_THRESHOLD:
            sla_violations += 1

        threshold_policy(utilization, cloud)

        response_times.append(response_time)
        costs.append(cost)
        vms.append(cloud.vms)

    return response_times, costs, vms, sla_violations


def run_rl():
    cloud = CloudEnvironment()
    agent = RLScaler()
    response_times, costs, vms = [], [], []
    sla_violations = 0

    for t in range(100):
        workload = generate_workload(t)
        utilization, response_time, cost = cloud.step(workload)

        if response_time > SLA_THRESHOLD:
            sla_violations += 1

        state = agent.get_state(utilization, cloud.vms)
        action = agent.choose_action(state)

        if action == 0:
            cloud.scale_down()
        elif action == 2:
            cloud.scale_up()

        sla_penalty = 5 if response_time > SLA_THRESHOLD else 0
        reward = -response_time - cost - sla_penalty
        next_state = agent.get_state(utilization, cloud.vms)
        agent.update(state, action, reward, next_state)

        response_times.append(response_time)
        costs.append(cost)
        vms.append(cloud.vms)

    return response_times, costs, vms, sla_violations


if __name__ == "__main__":
    th_rt, th_cost, th_vms, th_sla = run_threshold()
    rl_rt, rl_cost, rl_vms, rl_sla = run_rl()

    from plots import compare
    compare(th_rt, rl_rt, "Response Time Comparison", "Response Time")
    compare(th_cost, rl_cost, "Cost Comparison", "Cost")
    compare(th_vms, rl_vms, "VM Count Comparison", "Number of VMs")

    print("\n=== PERFORMANCE SUMMARY ===")
    print(f"Threshold Avg Response Time: {sum(th_rt)/len(th_rt):.2f}")
    print(f"RL Avg Response Time: {sum(rl_rt)/len(rl_rt):.2f}")
    print(f"Threshold Avg Cost: {sum(th_cost)/len(th_cost):.2f}")
    print(f"RL Avg Cost: {sum(rl_cost)/len(rl_cost):.2f}")
    print(f"Threshold SLA violations: {th_sla}")
    print(f"RL SLA violations: {rl_sla}")
