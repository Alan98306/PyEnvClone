import os, sys, math, glob, shutil
import numpy
import pandas
import selenium
import beautifulsoup4
import pyperclip
import pyautogui
# import pyinstaller
import plotly

import plotly.express as px
import plotly.graph_objects as go
from IPython.display import HTML

df_data = px.data.iris()
df_data
fig = px.histogram(df_data, x="sepal_width")
HTML(fig.to_html())
print('Hello Wolrd!')