# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: Code that will impress u ;)
# HEADERS ================================================================

import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from typing import List

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def section(section_name:str = "SECTION") -> None:
	section_name = f"\n {section_name} {'-' * (40 - len(section_name))}\n"
	print(section_name)

# ========================================================================
# FUNCTIONS 
# ========================================================================



# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")

	nodes_blue:List[str] = ['D','F','I','N','S']
	nodes_green:List[str] = ['BIH', 'GEO', 'ISR', 'MNE', 'SRB', 'CHE', 'TUR', 'UKR', 'GBR', 'AUS', 'HKG', 'USA']
	nodes_yellow:List[str] = ['AUT', 'BEL', 'BGR', 'HRV', 'CZE', 'EST', 'FRA', 'DEU', 'GRC', 'HUN', 'IRL', 'ITA', 'LVA', 'LUX', 'NLD', 'PRT', 'ROU', 'SVK', 'SVN', 'ESP']

	file_name:str = r"references/networks_assignment.csv"
	df:pd.DataFrame = pd.read_csv(file_name, index_col=0)

	G:nx.DiGraph = nx.DiGraph()

	for col in df.columns:
		col:str = str(col)
		color_str:str = "yellow"
		if col in nodes_blue:
			color_str = "blue"
		elif col in nodes_green:
			color_str = "green"
		G.add_node(col, color=color_str)

	for col in df.columns:
		for row in df[col].index:
			edge_weight:int = df.at[row, col]
			if edge_weight > 0:
				# print(f"{col}, {row}, {df.at[row, col]}")
				G.add_edge(col, row, weight = edge_weight)

	node_colors = [G.nodes[n]['color'] for n in G.nodes]
	nx.draw(G, with_labels=True, node_color=node_colors)
	plt.show()

	section("END")