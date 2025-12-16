from cloud_env import CloudEnvironment
from workload import generate_workload, predict_workload
from threshold_scaling import threshold_policy
from rl_scaling import RLScaler


def run(mode="bursty", sla=4.0, epsilon=0.1, steps=100):
    cloud_t = CloudEnvironment()
    cloud_r = CloudEnvironment()
    rl = RLScaler(epsilon)

    metrics = {
        "th_rt": [], "rl_rt": [],
        "th_cost": [], "rl_cost": [],
        "th_vms": [], "rl_vms": [],
        "th_sla": 0, "rl_sla": 0
    }

    for t in range(steps):
        load = generate_workload(t, mode)
        predicted = predict_workload()

        # -------------------------------
        # THRESHOLD-BASED SCALING
        # -------------------------------
        util, rt, cost, sla_v = cloud_t.step(load, sla)

        if sla_v:
            metrics["th_sla"] += 1

        threshold_policy(util, cloud_t)

        metrics["th_rt"].append(rt)
        metrics["th_cost"].append(cost)
        metrics["th_vms"].append(cloud_t.vms)

        # -------------------------------
        # RL-BASED SCALING (SAFE RL)
        # -------------------------------
        util, rt, cost, sla_v = cloud_r.step(load, sla)

        # 🔒 HARD SLA SAFETY GUARD
        if rt > sla:
            cloud_r.scale_up()

        if sla_v:
            metrics["rl_sla"] += 1

        state = rl.state(util, cloud_r.vms, predicted)
        action = rl.act(state)

        if action == 0:
            cloud_r.scale_down()
        elif action == 2:
            cloud_r.scale_up()

        # Multi-objective + SLA-aware reward
        reward = -(0.4 * rt + 0.2 * cost + 0.4 * (10 if sla_v else 0))

        next_state = rl.state(util, cloud_r.vms, predicted)
        rl.learn(state, action, reward, next_state)

        metrics["rl_rt"].append(rt)
        metrics["rl_cost"].append(cost)
        metrics["rl_vms"].append(cloud_r.vms)

        # Optional: stop exploration after warm-up
        if t > 20:
            rl.epsilon = 0.0

    return metrics
