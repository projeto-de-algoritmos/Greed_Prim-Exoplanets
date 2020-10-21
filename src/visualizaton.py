import plotly.graph_objects as go
import pandas as pd
import csv
import random

df_data = pd.read_csv('../pre-processing/planets_xyz_values.csv')

df_data['d'] = 3.26156 * df_data['d']

x_lines = list()
y_lines = list()
z_lines = list()

pairs = []
distances = []

with open('mst_distances_new.csv', 'r') as read:
    csv_read = csv.reader(read, delimiter=',')
    for row in csv_read:
        for item in row:
            distances.append(3.26156 * float(item))
            distances.append(3.26156 * float(item))
            distances.append(None)

with open('mst_generator.csv', 'r') as csv_read:
    csv_reader = csv.reader(csv_read, delimiter=',')
    for row in csv_reader:
        for field in row:
            pairs.append((row[0], field))

for p in pairs:
    for i in p:
        x_lines.append(float(df_data.loc[df_data['pl_name'] == i]['x']))
        y_lines.append(float(df_data.loc[df_data['pl_name'] == i]['y']))
        z_lines.append(float(df_data.loc[df_data['pl_name'] == i]['z']))
    x_lines.append(None)
    y_lines.append(None)
    z_lines.append(None)

layout = go.Layout(
    scene=dict(
        xaxis=dict(title='x', range=[-7500, 2200]),
        yaxis=dict(title='y', range=[-2700, 1200]),
        zaxis=dict(title='z', range=[-4700, 2000]),
        aspectmode='cube'),
)

fig = go.Figure(data=[go.Scatter3d(x=df_data['x'],
                                   y=df_data['y'],
                                   z=df_data['z'],
                                   name='',
                                   mode='markers',
                                   marker=dict(color=[
                                       f'rgb({random.randint(0, 256)}, {random.randint(0, 256)}, {random.randint(0, 256)})'
                                       for _ in range(4283)]),
                                   hovertemplate='<b>Name</b>: %{text}<br>Distance to Earth: %{customdata} light-years',
                                   text=df_data['pl_name'],
                                   customdata=df_data['d'],
                                   ),
                      go.Scatter3d(x=(0, 0),
                                   y=(0, 0),
                                   z=(0, 0),
                                   name='',
                                   mode='markers',
                                   hovertemplate='<b>Name</b>: Earth<br>',
                                   surfacecolor='red'),
                      go.Scatter3d(x=x_lines,
                                   y=y_lines,
                                   z=z_lines,
                                   text=distances,
                                   hovertemplate='<b>Distance</b>: %{text} light-years',
                                   mode='lines',
                                   name='')], layout=layout)

fig.show()
