def threshold_policy(utilization, cloud):
    if utilization > 0.7:
        cloud.scale_up()
    elif utilization < 0.3:
        cloud.scale_down()
