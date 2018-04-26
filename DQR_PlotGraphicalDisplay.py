import plotly
import plotly.graph_objs as go
import numpy

def generate_graphs(datas, names, is_continuous, list_of_cardinalities):
    for feature in names:
        keys = list(list_of_cardinalities[feature].keys())
        if is_continuous and len(list_of_cardinalities[feature]) >= 10:
            # We create a histogram.
            chart = [go.Histogram(
                x = list(datas[feature])
            )]
        else:
            # We create a bar plot.
            chart = [go.Bar(
                x = keys,
                y = list(list_of_cardinalities[feature].values())
            )]
        layout = go.Layout(
            title=feature,
        )

        fig = go.Figure(data=chart, layout=layout)
        plotly.offline.plot(fig, filename="./Visualisations/"+feature+".html")
