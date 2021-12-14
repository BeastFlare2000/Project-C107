import pandas as pd
import plotly.express as px
import csv

df = pd.read_csv("data.csv")
fig = px.scatter(x="student_id", y="level")
fig.show()