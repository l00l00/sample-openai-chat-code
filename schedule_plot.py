import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Define the time blocks and their durations in hours
schedule = [
    ("Promedis", 13, 14, "#6A5ACD"),
    ("Lunch / Rest", 14, 15, "#FFD700"),
    ("Freelancer", 15, 16.5, "#20B2AA"),
    ("Nap", 16.5, 17, "#D3D3D3"),
    ("n8n-rene", 17, 18.5, "#FF8C00"),
    ("Break / Walk", 18.5, 19, "#ADD8E6"),
    ("Review & Completion", 19, 21.5, "#32CD32"),
    ("Wind-down / Bed Prep", 21.5, 23, "#F08080")
]

# Prepare the plot
fig, ax = plt.subplots(figsize=(12, 2))
for task, start, end, color in schedule:
    ax.barh(0, end - start, left=start, height=0.5, color=color, edgecolor='black')
    ax.text((start + end) / 2, 0, task, va='center', ha='center', fontsize=9, color='black')

# Formatting
ax.set_xlim(13, 23)
ax.set_ylim(-0.5, 0.5)
ax.set_yticks([])
ax.set_xticks(range(13, 24))
ax.set_xticklabels([f"{h}:00" for h in range(13, 24)])
ax.set_title("📅 Shahab's Time Block (13:00 – 23:00)", fontsize=14, pad=15)

# Add legend
legend_patches = [mpatches.Patch(color=color, label=task) for task, _, _, color in schedule]
ax.legend(handles=legend_patches, bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()
