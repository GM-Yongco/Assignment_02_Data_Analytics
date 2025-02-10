import pandas as pd
import matplotlib.pyplot as plt

bar_df = pd.read_csv("references/bar_assignment.csv")

bar_df['COUNT'] = bar_df['COUNT'].map({1: "Yes", 0: "No"})

bar_pivot = bar_df.pivot_table(index="LABEL", columns="COUNT", aggfunc=len, fill_value=1)

fig, ax = plt.subplots(figsize=(8, 6))
bars = bar_pivot.plot(kind='barh', stacked=True, ax=ax, color=["red", "blue"])  

for bar_container in bars.containers:  
    for bar in bar_container:
        width = bar.get_width()  
        if width > 0:  
            ax.text(bar.get_x() + (width - 0.2),  
                    bar.get_y() + bar.get_height() / 2,  
                    int(width),
                    
                    ha='center', va='center', color='white', fontsize=12, fontweight='bold')

ax.grid(False) 
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.tick_params(axis='both', length=0)
ax.set_ylabel("")
ax.set_xlabel("")
ax.set_xticklabels(ax.get_xticklabels(), fontsize=12, fontweight="bold")  
ax.set_yticklabels(ax.get_yticklabels(), fontsize=12, fontweight="bold")  
ax.legend(ncols=2, bbox_to_anchor=(0, 1), loc='lower left', frameon=False)
ax.set_title(label="BARPLOT by S.M. Montañez & G. Yongco", y=1.1, loc="left")

plt.tight_layout()
plt.show()