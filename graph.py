import pandas as pd
from bokeh.plotting import figure, show, output_file
from datetime import datetime
import os

df = pd.read_csv('smile_records1.csv')
smile_ratios = list(df['smile_ratio'])


                

    
sm = [round(s, 3) for s in smile_ratios]
times = list(df['times'])
date_time = [datetime.strptime(d, '%Y-%m-%d %H:%M:%S.%f') for d in times]
p = figure(plot_width=800, plot_height=400, x_axis_type='datetime')
p.line(date_time, sm, alpha=0.5)
for s, d in zip(sm, date_time):
    if s > 2:
        p.circle(d, s, color="red", alpha=0.5, size=10)
show(p)
output_file('graph.html')
os.remove('smile_records1.csv')
print("done")

