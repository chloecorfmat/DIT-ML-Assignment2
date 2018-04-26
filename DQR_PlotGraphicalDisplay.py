import plotly
import plotly.graph_objs as go
import numpy

def generate_graphs(datas, names, is_continuous):
    for feature in names:
        unique = list(datas[feature])
        values = list()
        for u in unique:
            values.append(datas[feature].tolist().count(u))
        if is_continuous and len(unique) >= 10:
            # We create a histogram.
            chart = [go.Histogram(
                x = unique
            )]
        else:
            # We create a bar plot.
            chart = [go.Bar(
                x = numpy.asarray(unique),
                y = numpy.asarray(values)
            )]
        layout = go.Layout(
            title=feature,
        )

        fig = go.Figure(data=chart, layout=layout)
        plotly.offline.plot(fig, filename="./Visualisations/"+feature+".html")
