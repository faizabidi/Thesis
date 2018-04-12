import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np

x1 = ['Avg. Still FPS', 'Avg. Interactive FPS', 'Avg. Data Received (MBps)', 'Avg. Data Sent (MBps)', 'Avg. Memory (GB)']
y1 =[6.536, 52.073, 15.388, 0.587, 15.877]
error1=[0.039, 1.464, 2.241, 0.005, 0.110]

x2 = ['Avg. Still FPS1', 'Avg. Interactive FPS1', 'Avg. Data Received (MBps)', 'Avg. Data Sent (MBps)', 'Avg. Memory (GB)']
y2 =[0.783, 28.037, 7.322, 0.307, 17.077]
error2=[0.001, 1.751, 1.111, 0.007, 0.152]

# Create a trace
trace1 = go.Scatter(
    x = x1,
    y = y1,
    mode = 'markers+text',
    name='8 VTUs Files & 8 CPUs',
    text=y1,
    textposition='bottom left',
    #opacity=0.8,
    error_y=dict(
        type='data',
        array=error1,
        visible=True
    ),
)

trace2 = go.Scatter(
    x = x1,
    y = y2,
    mode = 'markers+text',
    name='16 VTU Files & 16 CPUs',
    text=y2,
    textposition='top right',
    #opacity=0.8,
    error_y=dict(
        type='data',
        array=error2,
        visible=True
    ),
)

data = [trace1, trace2]
layout = go.Layout(
    legend=dict(x=0.4, y=1.1),
    yaxis = dict(zeroline = False),
    xaxis = dict(zeroline = False),
)
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='basic-scatter')
