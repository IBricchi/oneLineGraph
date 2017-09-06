# One Line Grapher
One line grapher is a simple graphing tool built on top of the plotly python library and uses both numpy and scipy to take care of calculations. It combines all of the elements of graphing something using plotly but simplifies it by taking car of all of the extra processing required to make a graph be functional.

```
olg(
    x = <list> *required -see section 1.1
    y = <lis> *required -see section 1.1
    graph_type = <string> *required -see section 1.2
    title = <title> -see section 1.3
    x_axis = <boolean> -see section 1.4
    x_axis_title = <string> -see section 1.4
    y_axis = <boolean> -see section 1.4
    y_axis_title = <string> -see section 1.4
    trace_name = <string> -see secion 1.5
    mode = <string> -see section 3.1
    trendline = <boolean> -see section 3.2
    trendtype = <string> -see section 3.2.1
    trend_intercept = <boolean> -see section 3.2.2
    trend_intercept_val = <int> -see section 3.2.2
    show_trend_formula = <boolean> -see section 3.2.3  
)
```
## 1) The basics
These are the most important parts of the graph, a decent graph can be made using only these parts of the function
### 1.1) Axis Values
```
olg(
    x = <list> *required
    y = <list> *required
    ...
)
```
Both the x-axis and y-axis values are defined by the x and y parameters of the olg function. Each should can be introduced into the function by either a list of floats, or a numpy array of floats.

### 1.2) Graph type
```
olg(
    ...
    graph_type = <sting> *required
    ...
)
```

Possible graph types are currently limited to
1. [Scatter](#21-scatter-plots)

Each of these has it's own special use more information can about each type of graph can be found by looking for [section 2](#2-graph-types) subsection whatever position in the list the graph is in.

### 1.3) Graph title
```
olg(
    ...
    title = <string>
    ...
)
```
The graph title can be any string, if not specified it will be displayed as 'Graph'. If no title is desired just right input a space.
### 1.4) Axes
```
olg(
    ...
    x_axis = <boolean>
    x_axis_title = <string>
    y_axis = <boolran>
    y_axis_title = boolean
    ...
)
```
Currently changes to the axes are limited to naming them in future implementations I hope to add control over sizing as well as text formatting of mathematical symbols such as square roots and powers

The boolean parameters x_axis, and y_axis each represent wether that axis will have a title. Both are set to False as default

The string values x_axis_title, and y_axis_title each represent the text that will be labeling their respective axis, the default value is the name of the axis
### 1.5) Traces

```
olg(
    ...
    trace_name = <sting>
    ...
)    
```

The trace name is simply the value assigned to the group of data, currently only one input trace can be processed at a time. This name will appear in the legend when displaying the graph.
## 2) Graph types
### 2.1) Scatter plots
Scatter plots are graphs where the information is plotted on a two dimensional plane. These are very useful for visualising correlations between the value pairs being used. For information on how to plot this type of graph go to [section 3](#3scatter-plots)

## 3)Scatter Plots
Using the olg function we can define our scatter plot by setting the graph type to ``graph_type = 'scatter'``. This type of graph has several special parameter which affect how the graph will look, and will also return extra information if so desired.
### 3.1) Mode
```
olg(
    ...
    mode = <string>
    ...
)
```
The mode parameter instructs the function on how to display the input values given. The default variable is ```mode = 'markers'``` which will show all points as just that, points. Other modes include 
```
mode = 'line' #conects the points
```
For a full list of modes please read the [Plotly Documentation](https://plot.ly)

### 3.2) Trendlines
Trendlines are an extreamly usefull tool for data analytics, and provide a unique insight into the correlation of data. Fortunately I have included a simple way to create trendlines as well as display the function which defines it.
To tell the olg function that you require a trendline simply set ```trendline = True```, the trendline parameter is set to False by default
#### 3.2.1) Trend type
```
olg(
    ...
    trend_type = <string>
    ...
```
The trend_type parameter is used to define what type of trend line should be used, by default it is set to linear. The current options available are.
1. Linear

For more information on a how to use a particular type of trendline refer yourself to section 3.2.1 subsection whatever position in the list the trendline is in.

##### 3.2.1.1) Linear Trendlines
Linear trendline are the simplest of the trendlines and show a linear correlation they allow for simple analysis of data. To use this type of trendline the trend_type parameter should be set to ```trend_type = 'linear'`` are displayed using the linear function ```y = mx + c```. The basic linear trendline
###### 3.2.1.1.1) Intercept
```
olg(
    ...
    trend_intercept = <boolean>
    trend_intercept_val = <int>
    ...
)
```
To add a set intercept to the trendline simply set the trend_intercept parameter to True, and then set the trend_intercept_val to the y-intercept value. Currently only intercept at 0 is functional, and all other values will be turned into 0. The default values for these parameter are False and 0 respectively.