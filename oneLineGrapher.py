import plotly.graph_objs as go
from scipy import stats

def oneLineGrapher(x, y, type, title='Graph', trace_name='Trace', mode='markers', trendline=True, trend_type='linear'):
	if type == 'scatter':
		#Basic Data
		trace = go.Scatter(
			x = x,
			y = y,
			mode = mode,
			name = trace_name
			)

		layout = go.Layout(
			title = title
			)
		data = [trace]
		layout = [layout]
		return data, layout