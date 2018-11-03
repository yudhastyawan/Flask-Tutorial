from bokeh.layouts import column
from bokeh.models import CustomJS, ColumnDataSource, Slider
from bokeh.plotting import Figure, output_file, show, curdoc
from bokeh.embed import components

# output_file("js_on_change2.html")

file = open('data1.txt','r')
data = file.readlines()
for i in range(len(data)):
    data[i] = data[i].split()
file.close()

x = []
for i in range(len(data)):
    x.append(float(data[i][0]))
y = x

source = ColumnDataSource(data=dict(x=x,y=y))

plot = Figure(plot_width=400, plot_height=400)
plot.line('x','y',source = source, line_width=3, line_alpha=0.6)

callback = CustomJS(args=dict(source=source), code="""
    var data = source.data;
    var f = cb_obj.value
    var x = data['x']
    var y = data['y']
    for (var i = 0; i < x.length; i++){
        y[i] = Math.pow(x[i], f)
    }
    source.change.emit()
""")

slider = Slider(start=0.1, end=4, value=1, step=.1, title='power')
slider.js_on_change('value', callback)

layout = column(slider, plot)

# show(layout)
# curdoc().add_root(layout)
script, div = components(layout)
# print(script)
# print(div)