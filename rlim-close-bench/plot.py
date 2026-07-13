#!/usr/bin/env python3
"""naive close() 性能对比图：横坐标 rlim_cur，纵坐标 naive(ms)，多机型对比。"""
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

plt.rcParams["font.family"] = ["Arial", "Helvetica", "DejaVu Sans"]

rlim = [204800, 409600, 1048576]

# (label, cpu, ip, color, marker, naive_ms[])
series = [
    ("SA3", "AMD EPYC Milan (2.55/3.5GHz)", "30.49.40.64",
     "#E4572E", "o", [13.2071, 26.9422, 67.6947]),
    ("SA5", "AMD EPYC Bergamo (-/3.1GHz)", "21.245.122.28",
     "#F3A712", "s", [12.3957, 24.6781, 62.8519]),
    ("S5",  "Intel Xeon Cascade Lake 8255C (2.5/3.1GHz)", "11.177.159.161",
     "#2E86AB", "^", [95.7748, 191.6635, 499.0416]),
    ("S6",  "Intel Ice Lake (2.7/3.3GHz)", "30.49.239.225",
     "#3CB371", "D", [14.0108, 28.0092, 71.7231]),
    ("SA9", "AMD EPYC Turin-D (-/3.4GHz)", "11.152.253.72",
     "#8E44AD", "v", [13.4291, 26.4631, 67.7505]),
]

fig, ax = plt.subplots(figsize=(11, 7), dpi=160)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

for label, cpu, ip, color, marker, y in series:
    ax.plot(rlim, y, marker=marker, markersize=8, linewidth=2.2,
            color=color, label=f"{label}  ·  {cpu}",
            markerfacecolor=color, markeredgecolor="white", markeredgewidth=1.0)

ax.set_xscale("log")
ax.set_yscale("log")

# x 轴刻度：只标注实际数据点
ax.set_xticks(rlim)
def fmt_x(v, _):
    if v >= 1e9:
        return f"{v/1e9:.3f}B\n(RLIM_INFINITY)"
    if v >= 1e6:
        return f"{v/1e6:.3f}M"
    return f"{int(v/1000)}K"
ax.xaxis.set_major_formatter(FuncFormatter(fmt_x))
ax.minorticks_off()

def fmt_y(v, _):
    if v >= 1000:
        return f"{v/1000:g}k"
    return f"{v:g}"
ax.yaxis.set_major_formatter(FuncFormatter(fmt_y))

ax.set_xlabel("rlim_cur (RLIMIT_NOFILE soft limit)", fontsize=12, fontweight="bold")
ax.set_ylabel("naive close() latency (ms, log scale)", fontsize=12, fontweight="bold")
ax.set_title("naive close(0..rlim_cur) Performance vs rlim_cur\n"
             "Tencent S-series (kernel: tlinux 2.6, real_fds=5)",
             fontsize=14, fontweight="bold", pad=14)

ax.grid(True, which="major", linestyle="--", linewidth=0.6, alpha=0.5)
ax.grid(True, which="minor", linestyle=":", linewidth=0.4, alpha=0.25)

leg = ax.legend(title="Machine model · CPU", loc="upper left",
                fontsize=9.5, title_fontsize=10.5, framealpha=0.95,
                edgecolor="#cccccc")
leg.get_title().set_fontweight("bold")

fig.tight_layout()
out = "/Users/sasalu_1/.workbuddy/ai-artifacts/rlim-close-bench/rlim_close_naive_compare.png"
fig.savefig(out, bbox_inches="tight", facecolor="white")
print("saved:", out)
