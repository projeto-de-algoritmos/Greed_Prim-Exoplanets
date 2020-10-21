import pandas as pd
import plotly.express as px

df = pd.read_csv('../pre-processing/planets_xyz_values_reduce.csv')
df.head()

fig = px.scatter_3d(df, x='x', y='y', z='z',
                    color='planet',
                    title="3D Scatter Plot")
fig.show()
