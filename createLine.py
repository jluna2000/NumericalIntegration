from dash import dcc
# import dash_html_components as html
from dash import html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

def createLine(x_data, y_data, tittle):
    d = {'X': x_data, 'Y': y_data}
    df = pd.DataFrame(data=d)
    fig1 = px.line(df,'X','Y', title = tittle) 
    fig1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#00aaff')
    fig1.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='#00aaff')
    fig1.update_traces(line_color='#bb86fc')
    
    #xaxes='Opacity 0.5'
    fig1.update_layout({
        'plot_bgcolor': '#454545',
        
      #  'paper_bgcolor': 'rgba(0,0,0,0)',
       # dark grey 'paper_bgcolor': '#2c2c40',
       #'paper_bgcolor': '#0000ffff',
       'paper_bgcolor': '#121212',
        #'title': tittle
        'title_font_color': 'white',
        'font_color':'#bb86fc'
        #'paddding': 4,
        
    })
    layout = go.Layout(
  margin=go.layout.Margin(
        l=20, #left margin
        r=0, #right margin
        b=0, #bottom margin
        t=0  #top margin
    )
)
    return fig1