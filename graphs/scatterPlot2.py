import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np

x1 = ['Avg. Still FPS1', 'Avg. Interactive FPS1', 'Avg. Data Received (MBps)', 'Avg. Data Sent (MBps)', 'Avg. Memory (GB)']
y1 =[0.783, 28.037, 7.322, 0.307, 17.077]
error1=[0.001, 1.751, 1.111, 0.007, 0.152]

# Create a trace
trace1 = go.Scatter(
    x = x1,
    y = y1,
    mode = 'markers+text',
    text=y1,
    textposition='top right',
    marker=dict(
        color='rgb(100, 27, 21)',
        ),
    opacity=0.8,
    error_y=dict(
            type='data',
            array=error1,
            visible=True
        )
)

data = [trace1]
#layout = go.Layout(showlegend=True)
#fig = go.Figure(data=data, layout=layout)
# Plot and embed in ipython notebook!
py.plot(data, filename='16-16')

# or plot with: plot_url = py.plot(data, filename='basic-line')