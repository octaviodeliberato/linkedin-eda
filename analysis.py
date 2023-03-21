# IMPORTS 1 --------------------------------------------------------------------

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Get Connections Data --------------------------------------------------------
network = pd.read_csv('data/Connections.csv')
network.head(10)
network.info()

# Convert 'Connected On' to datetime
network['Connected On'] = pd.to_datetime(network['Connected On'])

# Nr of connectons over time
plot_dat = network.groupby(by='Connected On').count().reset_index()

connections_line = px.line(plot_dat, 
                           x="Connected On", 
                           y="First Name", 
                           labels={'First Name': 'Number'},
                           title='My Connections')
connections_line.show()

