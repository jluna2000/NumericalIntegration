import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np
from squareTest import power2, addHello
from createLine import createLine
from mathFunction import f, simpsonsIntegration

external_stylesheets = [
    {
        'href': "https://fonts.googleapis.com/css2?family=Inter&family=Poppins:wght@700&display=swap",
        'rel': 'stylesheet',
        'crossorigin': 'anonymous'
    }
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# fig = []

x = np.linspace(-5, 5, 1000, endpoint=False)
x = x.tolist()
y = []

for i in x:
    y.append(i**2)
fig = createLine(x, y, 'Function')

app.layout = html.Div(
    [
        html.H1(children = "The Numerical Integration Calculator"),
        html.P("This numerical integration calculator makes use of the Composite Simpson's " 
        "Rule to estimate the definite integral of the inputted function within the specified bounds. "
        "This calculator is set up to have 100 subintervals in between 1 point: an interval every 0.01 "
        "For more information on the Simpson's Rule, click the button below.", id="description"),
        html.Br(),
        html.Br(),
        html.Div([
            html.P("Function"),
            dcc.Input(id="mathFunction", type="text", placeholder="Function", className="textbox"),
            html.Br(),
            html.P("Bound 1"),
            dcc.Input(id="bound1", type="number", placeholder="a", value=-5, className="textbox"),
            html.P("Bound 2"),
            dcc.Input(id="bound2", type="number", placeholder="b", value=5, className="textbox"),
            html.Table(
                [
                    html.Tr([
                        html.Td(html.Div("Numerical Integration: ")),
                        html.Td(html.Div("0", id="integral-out"))
                    ])
                ]
            )
            # html.Div("0", id="integral-out"),

        ], id="textBoxes"),
        html.Hr(),
        dcc.Graph(
            id='FunctionGraph',
            figure = fig  
        )
    ]
)

@app.callback(
    Output("integral-out", "children"),
    Input("mathFunction", "value"),
    Input("bound1", "value"),
    Input("bound2", "value")
)
def squareNumber(sqval, b1, b2):
    integrationAnswer = simpsonsIntegration(sqval, b1, b2, int((b2 - b1)*100))
    return round(integrationAnswer, 5)

@app.callback(
    Output("FunctionGraph", "figure"),
    Input("mathFunction", "value"),
    Input("bound1", "value"),
    Input("bound2", "value")
)
def chooseFunction(funval, b1, b2):
    x = np.linspace(b1, b2, int((b2 - b1)*100), endpoint=False)
    result = []
    if 'x' in funval:
        for i in x:
            result.append(f(i, funval))
        return createLine(x, result, 'Function')
    else:
        return fig

if __name__ == "__main__":
    app.run_server()