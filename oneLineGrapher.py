import plotly.graph_objs as go

import numpy as np
from scipy import stats


def olg(x, y, graph_type, title='Graph', x_axis=True, x_axis_title='x-axis', y_axis=True, y_axis_title='y-axis', trace_name='Trace', mode='markers', trendline=False, trend_type='linear',
        trend_intercept=False, trend_intercept_val=0):
    x, y = np.array(x), np.array(y)
    if graph_type == 'scatter':
        data, layout = scatter(
            x=x,
            y=y,
            title=title,
            x_axis=x_axis,
            x_axis_title=x_axis_title,
            y_axis=y_axis,
            y_axis_title=y_axis_title,
            trace_name=trace_name,
            mode=mode,
            trendline=trendline,
            trend_type=trend_type,
            trend_intercept=trend_intercept,
            trend_intercept_val=trend_intercept_val
        )
    return data, layout


def scatter(x, y, title, x_axis, x_axis_title, y_axis, y_axis_title, trace_name, mode, trendline, trend_type, trend_intercept, trend_intercept_val):
    print(trend_intercept_val)
    data, layout = [], []
    # Basic Data
    trace = go.Scatter(
        x=x,
        y=y,
        mode=mode,
        name=trace_name
    )
    data.append(trace)
    # trendline
    if trendline:
        trendline_trace = draw_trendline(
            x=x,
            y=y,
            trend_type=trend_type,
            intercept=trend_intercept,
            intercept_val=trend_intercept_val
        )
        data.append(trendline_trace)

    layout_settings = scatter_layout(
        title=title,
        x_axis=x_axis,
        x_axis_title=x_axis_title,
        y_axis=y_axis,
        y_axis_title=y_axis_title
    )
    layout.append(layout_settings)
    return data, layout


def scatter_layout(title, x_axis, x_axis_title, y_axis, y_axis_title):
    x_axis_dict = dict()
    if x_axis: x_axis_dict['title'] = x_axis_title

    y_axis_dict = dict()
    if y_axis: y_axis_dict['title'] = y_axis_title
    layout_settings = go.Layout(
        title=title,
        xaxis=x_axis_dict,
        yaxis=y_axis_dict
    )
    return layout_settings


def draw_trendline(x, y, trend_type, intercept, intercept_val):
    if trend_type == 'linear':
        x, y = linear_trendline(
            x=x,
            y=y,
            intercept=intercept,
            intercept_val=intercept_val
        )
    trendline_trace = go.Scatter(
        x=x,
        y=y,
        mode='line',
        name='Trendline',
    )
    return trendline_trace


def linear_trendline(x, y, intercept, intercept_val):
    if intercept is None:
        m, c = linreg(
            x=x,
            y=y
        )
        x = [0, x[-1]]
    else:  # intercept == 0:
        m, c = linreg(
            x=x,
            y=y,
            intercept=intercept,
            intercept_val=intercept_val
        )
        x = [0, x[-1]]
    y = [m * x_val + c for x_val in x]
    return x, y


def linreg(x, y, intercept=False, intercept_val=0):
    if intercept:
        if intercept_val == 0:
            x = x[:, np.newaxis]
            m, _, _, _ = np.linalg.lstsq(x, y)
            m = m[0]
            c = intercept_val
    else:
        m, c, r, p, stderror = stats.linregress(x, y)
    return m, c
