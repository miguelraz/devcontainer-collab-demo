"""
Pirates vs. CO2 Concentration
------------------------------
A satirical illustration of spurious correlation [1].
As the number of pirates falls, atmospheric CO2 rises.
Correlation does not imply causation [2].

[1] Vigen, T. (2015). Spurious Correlations. Hachette Books.
[2] Pearl, J. (2009). Causality. Cambridge University Press.
"""

import matplotlib.pyplot as plt
import numpy as np

# Year of observation.
years = np.array([1820, 1860, 1880, 1920, 1950, 1980, 2000, 2010, 2020])

# Estimated global pirate count (thousands). Dummy data.
pirates = np.array([45, 30, 20, 15, 5, 3, 2, 1.5, 1])

# Atmospheric CO2 concentration (parts per million, ppm). Dummy data
# calibrated loosely to the Keeling Curve [3].
# [3] Keeling, C. D. (1958). Tellus, 10(2), 200-203.
co2_ppm = np.array([285, 288, 292, 305, 310, 338, 370, 390, 412])

fig, ax1 = plt.subplots(figsize=(10, 6))

# --- Left axis: pirates ---
color_pirates = "#1f77b4"
ax1.set_xlabel("Year", fontsize=13)
ax1.set_ylabel("Pirates (thousands)", color=color_pirates, fontsize=13)
ax1.plot(
    years,
    pirates,
    "o-",
    color=color_pirates,
    linewidth=2,
    markersize=7,
    label="Pirates",
)
ax1.tick_params(axis="y", labelcolor=color_pirates)
ax1.set_ylim(0, pirates.max() * 1.2)

# --- Right axis: CO2 ---
color_co2 = "#d62728"
ax2 = ax1.twinx()
ax2.set_ylabel("CO₂ Concentration (ppm)", color=color_co2, fontsize=13)
ax2.plot(years, co2_ppm, "s--", color=color_co2, linewidth=2, markersize=7, label="CO₂")
ax2.tick_params(axis="y", labelcolor=color_co2)
ax2.set_ylim(270, co2_ppm.max() * 1.1)

# --- Annotations ---
fig.suptitle(
    "Global Pirate Population vs. Atmospheric CO₂", fontsize=15, fontweight="bold"
)
ax1.set_title(
    "A masterclass in spurious correlation", fontsize=11, style="italic", color="gray"
)

# Combine legends from both axes.
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="center left", fontsize=11)

ax1.grid(True, linestyle="--", alpha=0.4)
fig.tight_layout()

plt.savefig("pirates_vs_co2.png", dpi=150)
print("Plot saved to pirates_vs_co2.png")
plt.show()
