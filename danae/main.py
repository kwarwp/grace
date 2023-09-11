# grace.danae.main.py
from browser import document 
from browser import svg 
parte = document["um_desenho"]
tela = svg.svg(width=400, height=200)
parte <= tela
tela <= svg.rect(width=100, height=150, style={'fill': 'red'})
tela <= svg.circle(cx=200, cy=100, r=80, style={'fill': 'blue'})
tela <= svg.line(x1=110, y1=30, x2=120, y2=180, style={'stroke': 'green', 'stroke-width': '5px'})
tela <= svg.path(d="M320 20 l80 80 l-80 80 Z", style={'fill': 'magenta'})


