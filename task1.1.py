import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 100)


def position(t):
    return 2 * t ** 3 - 5 * t ** 2 + 10 * t + 2


h = t[1] - t[0]
velocity = np.gradient(position(t), h)

acceleration = np.gradient(velocity, h)

plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t, position(t), 'b')
plt.title('Position')
plt.xlabel('Time')
plt.ylabel('Position')

plt.subplot(3, 1, 2)
plt.plot(t, velocity, 'g')
plt.title('Velocity')
plt.xlabel('Time')
plt.ylabel('Velocity')

plt.subplot(3, 1, 3)
plt.plot(t, acceleration, 'r')
plt.title('Acceleration')
plt.xlabel('Time')
plt.ylabel('Acceleration')

plt.tight_layout()
plt.show()
