class CloudEnvironment:
    def __init__(self):
        self.vms = 2
        self.max_vms = 10
        self.min_vms = 1
        self.vm_capacity = 50  # workload per VM
        self.cost_per_vm = 1

    def step(self, workload):
        capacity = self.vms * self.vm_capacity
        utilization = min(workload / capacity, 1.0)

        response_time = 1 + utilization * 5
        cost = self.vms * self.cost_per_vm

        return utilization, response_time, cost

    def scale_up(self):
        if self.vms < self.max_vms:
            self.vms += 1

    def scale_down(self):
        if self.vms > self.min_vms:
            self.vms -= 1
