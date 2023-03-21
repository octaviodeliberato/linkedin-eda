import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

network = pd.read_csv('data/Connections.csv')
network.head(10)