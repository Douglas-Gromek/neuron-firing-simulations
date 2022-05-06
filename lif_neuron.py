import matplotlib.pyplot as plt
import numpy as np

inputCurrent = 1                   # A
restingVoltage = 0                 # mV
thresholdVoltage = 20              # mV
membPot = restingVoltage           # mV
capacitance = 1                    # Micro Farads/Cm^2
resistance = 64                    # Ohm
tau = resistance * capacitance     # ms
plotList = [(0, 0)]                # Hold all plot points
time = np.linspace(1, 50, 50)      # Time intervals

for t in time:
    membPot = membPot + (inputCurrent - (membPot / resistance)) / capacitance
    if membPot >= thresholdVoltage:  # simulate a spike
        membPot += 20
        plotList.append((t, membPot))
        membPot = restingVoltage
    plotList.append((t, membPot))

x_val = [x[0] for x in plotList]
y_val = [x[1] for x in plotList]
plt.plot(x_val, y_val)
plt.title("Simulation of a Leaky Integrate-and-Fire Neuron")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane Potential (V)")
plt.show()