import numpy as np
import pandas as pd
from pandas import read_csv
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('ggplot')

file = "Topic_Survey_Assignment.csv"
data = pd.read_csv(file, index_col=0)

data.sort_values(by="Very interested", ascending=False, inplace=True)
totresponse = 2233
percentVI = [str(round(100 * (float(value) / totresponse), 2)) + '%' for value in data["Very interested"]]
percentSI = [str(round(100 * (float(value) / totresponse), 2)) + '%' for value in data["Somewhat interested"]]
percentNI = [str(round(100 * (float(value) / totresponse), 2)) + '%' for value in data["Not interested"]]
totpercents = percentVI + percentSI + percentNI

plt.rc('font', size=14)
plt.rc('axes', labelsize=14)
plt.rc('legend', fontsize=14)
plt.rc('xtick', labelsize=14)
plt.rc('figure', titlesize=16)

ax = data.plot(kind='bar', figsize=(20, 8), width=0.8, color=['#5cb85c', '#5bc0de', '#d9534f'])
ax.set_title("Percentage of Respondants' Interest in Data Science Areas")

ax.axes.get_yaxis().set_visible(False)
ax.set_facecolor('white')
ax.legend(facecolor='white', framealpha=1)

rects = ax.patches
labels = [totpercents[i] for i in range(len(rects))]
for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
            ha='center', va='bottom', fontsize=14)

plt.show()