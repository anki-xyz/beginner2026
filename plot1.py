import numpy as np
import matplotlib.pyplot as plt


def plot_sine_wave(freq=10, color='green', linestyle='--'):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * freq * x)

    plt.figure(figsize=(10, 6), facecolor='white')
    ax = plt.gca()
    ax.set_facecolor('white')

    ax.plot(x, y, label='For Frodo', color=color, linestyle=linestyle, linewidth=2)

    ax.set_title('Sine Wave')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.legend()
    ax.grid(False)

    plt.tight_layout()
    plt.show()


plot_sine_wave()
