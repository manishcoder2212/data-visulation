import pandas as m
import plotly.express as p


x=m.read_csv("data2.csv")
m=p.line(x,x='Year',y='Per capita income',color='Country',title='manish line graph')

m.show()