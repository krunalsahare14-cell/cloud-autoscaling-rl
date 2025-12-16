import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8")

def compare(th, rl, title, ylabel):
    plt.figure(figsize=(8, 4))
    plt.plot(th, label="Threshold-Based", linewidth=2)
    plt.plot(rl, label="RL-Based", linewidth=2)
    plt.xlabel("Time Steps")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(title.replace(" ", "_").lower() + ".png", dpi=300)
    plt.show()
