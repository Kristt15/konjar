import matplotlib.pyplot as plt
import numpy as np

f0 = 1.0
fs = 1000
durasi = 2.0
t = np.linspace(0, durasi, int(fs * durasi), endpoint=False)

harmonik_list = [1, 3, 5, 7, 9]

fig, axes = plt.subplots(
    nrows=len(harmonik_list) + 1,
    ncols=1,
    figsize=(10, 10),
    sharex=True,
    sharey=True,
)

gelombang_superposisi = np.zeros_like(t)

for idx, n in enumerate(harmonik_list):
    amplitudo = (4 / np.pi) / n        
    gelombang_n = amplitudo * np.sin(2 * np.pi * n * f0 * t)
    gelombang_superposisi += gelombang_n

    axes[idx].plot(
        t, gelombang_n,
        label=f"Harmonik ke-{n} (f = {n*f0:.1f} Hz, A = 4/({n}π))",
        color="royalblue", linewidth=1.2,
    )
    axes[idx].set_ylabel(f"H-{n}", fontsize=9)
    axes[idx].grid(True, linestyle="--", alpha=0.6)
    axes[idx].legend(loc="upper right", fontsize=8)

kotak_ideal = np.sign(np.sin(2 * np.pi * f0 * t))

axes[-1].plot(t, kotak_ideal, "--", color="gray", linewidth=1,
              label="Gelombang kotak ideal")
axes[-1].plot(t, gelombang_superposisi, color="crimson", linewidth=1.8,
              label=f"Superposisi {len(harmonik_list)} harmonisa")
axes[-1].set_ylabel("Total", fontsize=9)
axes[-1].set_xlabel("Waktu (detik)", fontsize=10)
axes[-1].grid(True, linestyle="--", alpha=0.6)
axes[-1].legend(loc="upper right", fontsize=8)

plt.suptitle("Visualisasi Harmonisasi Gelombang Sinus", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.show()

