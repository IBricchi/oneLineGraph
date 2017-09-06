import plotly.graph_objs as go

import numpy as np
from scipy import stats


def olg(x, y, graph_type, title='Graph', x_axis=True, x_axis_title='x-axis', y_axis=True, y_axis_title='y-axis',
        trace_name='Trace', mode='markers', trendline=False, trend_type='linear', trend_intercept=False,
        trend_intercept_val=0, show_trend_formula=False):
    x, y, extra = np.array(x), np.array(y), dict()
    if graph_type == 'scatter':
        data, layout, scatter_extra = scatter(
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
            trend_intercept_val=trend_intercept_val,
            show_trend_formula=show_trend_formula
        )
        extra['scatter'] = scatter_extra
    return data, layout, extra


def scatter(x, y, title, x_axis, x_axis_title, y_axis, y_axis_title, trace_name, mode, trendline, trend_type,
            trend_intercept, trend_intercept_val, show_trend_formula):
    data, layout, trend_formula, trend_label_x, trend_label_y, extra, empty_dict = [], [], '', 0.0, 0.0, dict(), dict()
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
        trendline_trace, trend_formula, trend_label_x, trend_label_y, trendline_extra = draw_trendline(
            x=x,
            y=y,
            trend_type=trend_type,
            intercept=trend_intercept,
            intercept_val=trend_intercept_val
        )
        extra['trendline'] = trendline_extra
        data.append(trendline_trace)

    layout_settings, layout_extra = scatter_layout(
        title=title,
        x_axis=x_axis,
        x_axis_title=x_axis_title,
        y_axis=y_axis,
        y_axis_title=y_axis_title,
        show_trend_formula=show_trend_formula,
        trend_formula=trend_formula,
        trend_label_x=trend_label_x,
        trend_label_y=trend_label_y
    )
    extra['layout'] = layout_extra
    layout.append(layout_settings)
    return data, layout, extra


def scatter_layout(title, x_axis, x_axis_title, y_axis, y_axis_title, show_trend_formula, trend_formula='',
                   trend_label_x=0.0, trend_label_y=0.0):
    x_axis_dict, y_axis_dict, anontations, trend_label, extra = dict(), dict(), [], dict(), dict()
    if x_axis:
        x_axis_dict['title'] = x_axis_title
    if y_axis:
        y_axis_dict['title'] = y_axis_title
    if show_trend_formula:
        trend_label = [
            dict(
                x=trend_label_x,
                y=trend_label_y,
                xref='x',
                yref='y',
                text=trend_formula,
                showarrow=True,
                arrowhead=7,
                ax=0,
                ay=-40
                )
            ]
        anontations += trend_label
    print(show_trend_formula)
    layout_settings = go.Layout(
        title=title,
        xaxis=x_axis_dict,
        yaxis=y_axis_dict,
        annotations=anontations
    )
    print(anontations)
    return layout_settings, extra


def draw_trendline(x, y, trend_type, intercept, intercept_val):
    extra = dict()
    if trend_type == 'linear':
        x, y, trend_formula, linear_extra = linear_trendline(
            x=x,
            y=y,
            intercept=intercept,
            intercept_val=intercept_val
        )
        trend_label_x, trend_label_y = x[-1] / 2, y[-1] / 2
        extra['linear'] = linear_extra
    trendline_trace = go.Scatter(
        x=x,
        y=y,
        mode='line',
        name='Trendline',
    )
    return trendline_trace, trend_formula, trend_label_x, trend_label_y, extra


def linear_trendline(x, y, intercept, intercept_val):
    extra = dict()
    if intercept is None:
        m, c, trend_formula, linereg_extra = linreg(
            x=x,
            y=y
        )
        x = [0, x[-1]]
        extra['linereg'] = linereg_extra
    else:  # intercept == 0:
        m, c, trend_formula, linereg_extra = linreg(
            x=x,
            y=y,
            intercept=intercept,
            intercept_val=intercept_val
        )
        extra['linereg'] = linereg_extra
        x = [0, x[-1]]
    y = [m * x_val + c for x_val in x]
    return x, y, trend_formula, extra


def linreg(x, y, intercept=False, intercept_val=0):
    extra = dict()
    if intercept:
        extra['intercept'] = intercept_val
        if intercept_val == 0:
            x = x[:, np.newaxis]
            m, _, _, _ = np.linalg.lstsq(x, y)
            m = m[0]
            c = intercept_val
            formula = ['y = ', str(m), 'x']
            formula = str.join('', formula)
            extra['m'], extra['c'], extra['formula'] = m, c, formula
    else:
        m, c, r, p, stderror = stats.linregress(x, y)
        formula = ['y = ', str(m), 'x + ', str(c)]
        formula = str.join('', formula)
        extra['m'], extra['c'], extra['formula'] = m, c, formula
    return m, c, formula, extra
