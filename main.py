
import numpy as np
import pandas as pd
import plotly.express as px

data = pd.read_csv('./SOCR-HeightWeight.csv')

mean = np.mean(data['Weight(Pounds)'])
median = np.median(data['Weight(Pounds)'])

print("Mean = ", mean)
print("Median = ", median)