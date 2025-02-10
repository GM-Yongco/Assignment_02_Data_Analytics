import pandas as pd
import plotly.graph_objects as go

sankey_df = pd.read_csv("references/sankey_assignment.csv") 

source_columns = ['PS', 'OMP', 'CNP', 'NRP', 'NMCCC', 'PEC', 'NCDM', 'RGS']
intermediate_nodes = ['S', 'I', 'D', 'F', 'N']
target_columns = ['Reg', 'Aca', 'Oth']

filtered_df = sankey_df[sankey_df['LABEL'].isin(intermediate_nodes)]
all_labels = source_columns + intermediate_nodes + target_columns
label_map = {label: i for i, label in enumerate(all_labels)}
source, target, value, link_colors = [], [], [], []

color_map = {
    'OMP': "rgba(108, 173, 168, 1)", 
    'PS': "rgba(231, 167, 135, 1)",  
    'CNP': "rgba(227, 150, 74, 1)",  
    'RGS': "rgba(162, 98, 199, 1)", 
    'NRP': "rgba(222, 123, 176, 1)", 
    'NCDM': "rgba(243, 216, 99, 1)",  
    'NMCCC': "rgba(159, 185, 150, 1)",  
    'PEC': "rgba(120, 196, 201, 1)",  
    'S': "rgba(162, 203, 243, 1)",  
    'I': "rgba(112, 187, 244, 1)",  
    'D': "rgba(199, 155, 158, 1)", 
    'F': "rgba(94, 128, 172, 1)",  
    'N': "rgba(117, 148, 224, 1)",
    'Aca': "rgba(192, 246, 170, 1)", 
    'Reg': "rgba(116, 174, 124, 1)",  
    'Oth': "rgba(181, 233, 161, 1)", 
}

for src in source_columns:
    for _, row in filtered_df.iterrows():
        inter = row['LABEL']
        flow_value = row[src]
        if flow_value > 0:
            source.append(label_map[src])
            target.append(label_map[inter])
            value.append(flow_value)
            link_colors.append(color_map[src])  

for _, row in filtered_df.iterrows():
    inter = row['LABEL']
    for tgt in target_columns:
        flow_value = row[tgt]
        if flow_value > 0:
            source.append(label_map[inter])
            target.append(label_map[tgt])
            value.append(flow_value)
            link_colors.append(color_map[inter])  

node_colors = [color_map[label] for label in all_labels]

fig = go.Figure(go.Sankey(
    node=dict(
        pad=15, thickness=20, line=dict(color="black", width=0.5),
        label=all_labels, color=node_colors  
    ),
    link=dict(
        source=source, target=target, value=value, color=link_colors  
    )
))

fig.update_layout(title_text="Sankey Diagram by S.M. Montañez & G. Yongco", font_size=10)
fig.show()