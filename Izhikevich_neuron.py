import matplotlib.pyplot as plt
import numpy as np

a = 0.10   # Time scale of recovery variable u
b = 0.2    # Sensitivity of u
c = -65    # After spike reset value of v
d = 8      # After-spike reset value of u
v = -65    # Membrane potential
u = b * v  # Membrane recovery variable

inputCurrent = 8
time = np.linspace(0, 50, 250)  # Time intervals
plotList = [(0, -65)]  # Hold all (t, membrane potential) tuples

for t in time:
    u = u + (a * (b * v - u))  # update membrane recovery variable and V
    v = v + (0.04 * (v ** 2) + (5 * v) + 140 - u + inputCurrent)

    if v >= 30:  # spike apex has occurred
        plotList.append((t, 30))  # Plot the spike
        v = c
        u = u + d
        plotList.append((t, v))  # Plot the reset to resting voltage
    else:
        plotList.append((t, v))

x_val = [x[0] for x in plotList]
y_val = [x[1] for x in plotList]
plt.plot(x_val, y_val)
plt.title("Simulation of a Izhikevich Neuron")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane Potential")
plt.show()