import plotly.graph_objs as go
from scipy import stats

def oneLineGrapher(x, y, type, title='Graph', trace_name='Trace', mode='markers', trendline=False, trend_type='linear', trend_intercept=None):
	data = []
	layout = []
	if type == 'scatter':
		#Basic Data
		trace = go.Scatter(
			x = x,
			y = y,
			mode = mode,
			name = trace_name
			)
		data.append(trace)
		if(trendline):
			if(trend_type == 'linear'):
				if(not trend_intercept):
					trendline_m, trendline_c = linreg(x,y)
					trendline_x = [0,x[-1]]
					trendline_y = [trendline_m * trendline_x[i] + trendline_c for i in range(0, len(trendline_x))]
					trendline_trace = go.Scatter(
						x=trendline_x,
					    y=trendline_y,
					    mode = 'line',
					    name = 'Trendline'
						)
					data.append(trendline_trace)

		layout_settings = go.Layout(
			title = title
			)
		layout.append(layout_settings)
		return data, layout

def linreg(x, y):
    slope, intercept, r, p, stderror = stats.linregress(x,y)
    return slope, intercept



    