import csv
import numpy as np
import pandas as pd
import windrose
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
filename = 'MET 2018.csv'
#pulls out data from csv
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    wind_direction, wind_speed = [], []
    for row in reader:
        #row number is row in csv
        if row[43]:
            ws = float(row[43])
            wind_speed.append(ws)

        if row[47]:
            wd = float(row[47])
            wind_direction.append(wd)

#Creates Visulization
print(wind_speed)
print(wind_direction)
print(len(wind_speed))
print(len(wind_direction))
ax = windrose.WindroseAxes.from_ax()
ax.bar(wind_direction, wind_speed, normed=True, opening=.9, edgecolor='black')
ax.set_legend(loc='upper right')
plt.show()