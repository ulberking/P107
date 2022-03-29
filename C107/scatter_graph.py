import pandas as pd
import plotly.express as pe
df =pd.read_csv('data.csv')
data = df.groupby(['student_id','level'],as_index=False)['attempt'].mean()
graph = pe.scatter(data,x='student_id',y='level',color='attempt',size="attempt")
graph.show()