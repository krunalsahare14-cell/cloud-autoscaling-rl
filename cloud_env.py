class CloudEnvironment:
    def __init__(self):
        self.vms = 2
        self.min_vms = 1
        self.max_vms = 10
        self.vm_capacity = 50
        self.cost_per_vm = 1

    def step(self, workload, sla_threshold):
        capacity = self.vms * self.vm_capacity
        utilization = min(workload / capacity, 1.0)

        response_time = 1 + utilization * 5
        cost = self.vms * self.cost_per_vm
        sla_violation = response_time > sla_threshold
        sla_penalty = 10 if sla_violation else 0

        total_cost = cost + sla_penalty
        return utilization, response_time, total_cost, sla_violation

    def scale_up(self):
        if self.vms < self.max_vms:
            self.vms += 1

    def scale_down(self):
        if self.vms > self.min_vms:
            self.vms -= 1
