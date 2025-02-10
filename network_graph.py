# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: Code that will impress u ;)
# HEADERS ================================================================

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

import math

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


def get_triangle_sides(hypotenuse, angle_degrees):
	round_to_decimal = 10

	angle_radians = math.radians(angle_degrees)
	height = round(hypotenuse * math.sin(angle_radians), round_to_decimal)
	length = round(hypotenuse * math.cos(angle_radians), round_to_decimal)
	return [height, length]

def polygon_vertices(number_of_sides = 5, radius = 10):
	angle_per_vertex = 360/number_of_sides
	coordinates:list = []
	for i in range(0,5):
		coordinates.append(get_triangle_sides(radius, angle_per_vertex*i))
	
	return coordinates

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
	new_node_colors = [G.nodes[each_node]['color'] for each_node in G.nodes]
	print(new_node_colors)

	for col in df.columns:
		for row in df[col].index:
			edge_weight:int = df.at[row, col]
			if edge_weight > 0:
				G.add_edge(col, row, weight = edge_weight)

	new_positions = nx.shell_layout(G)
	inner_circle_coords:list = polygon_vertices(radius=0.5)

	for i, center_node in enumerate(nodes_blue): 
		new_positions[center_node] = inner_circle_coords[i]
	print(new_positions)

	nx.draw(G, pos=new_positions, with_labels=True, node_color=new_node_colors)
	plt.show()



	section("END")