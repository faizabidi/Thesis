import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
    mode = 'markers+text',
    name='16 VTU Files and 16 CPUs',
)

trace1 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
    mode = 'markers+text',
    #name='16 VTU Files and 16 CPUs',
)

data = [trace0, trace1]
fig = go.Figure(data=data)

py.plot(fig, filename='default-legend')