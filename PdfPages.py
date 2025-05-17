from matplotlib.backends.backend_pdf import PdfPages

# Save the chart to a PDF file
pdf_path = "/mnt/data/Shahab_Time_Block_Schedule.pdf"
with PdfPages(pdf_path) as pdf:
    fig, ax = plt.subplots(figsize=(12, 2))
    for task, start, end, color in schedule:
        ax.barh(0, end - start, left=start, height=0.5, color=color, edgecolor='black')
        ax.text((start + end) / 2, 0, task, va='center', ha='center', fontsize=9, color='black')
    ax.set_xlim(13, 23)
    ax.set_ylim(-0.5, 0.5)
    ax.set_yticks([])
    ax.set_xticks(range(13, 24))
    ax.set_xticklabels([f"{h}:00" for h in range(13, 24)])
    ax.set_title("Shahab's Time Block (13:00 – 23:00)", fontsize=14, pad=15)
    legend_patches = [mpatches.Patch(color=color, label=task) for task, _, _, color in schedule]
    ax.legend(handles=legend_patches, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    pdf.savefig(fig)
    plt.close()

pdf_path
