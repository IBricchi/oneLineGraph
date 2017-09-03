import plotly.graph_objs as go

import numpy as np
from scipy import stats

def oneLineGrapher(x, y, type, title='Graph', trace_name='Trace', mode='markers', trendline=False, trend_type='linear', trend_intercept=None):
	x, y = np.array(x), np.array(y)
	data, layout = [], []
	if type == 'scatter':
		#Basic Data
		trace = go.Scatter(
			x = x,
			y = y,
			mode = mode,
			name = trace_name
			)
		data.append(trace)
		#trendline
		if(trendline):
			if(trend_type == 'linear'):
				if trend_intercept == None:
					trendline_m, trendline_c = linreg(
						_x = x,
						_y = y
						)
					trendline_x = [0,x[-1]]
				elif trend_intercept == 0:
					trendline_m, trendline_c = linreg(
						_x = x,
						_y = y,
						_intercept = 0
						)
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

def linreg(_x, _y, _intercept=None):
	if _intercept == 0:
		x = _x[:,np.newaxis]
		slope, _, _, _ = np.linalg.lstsq(x, _y)
		slope = slope[0]
		intercept = 0
	else:
		slope, intercept, r, p, stderror = stats.linregress(_x,_y)
	return slope, intercept



    