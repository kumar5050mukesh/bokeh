from flask import Flask, render_template

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE



app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/vbar')
def bokeh():


    fig = figure(width=600, height=600)
    fig.vbar(
        x=[8,4,9,12,15,17],
        width=0.5,
        bottom=0,
        top=[1.7, 2.2, 4.6, 3.9],
        color='red'
    )

    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # render template
    script, div = components(fig)
    return  render_template(
        'index.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    


if __name__ == '__main__':
    app.run(debug=True)
